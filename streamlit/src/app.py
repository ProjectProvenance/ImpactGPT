import os
import openai
import streamlit as st
from streamlit_chat import message

from driver import read_query, get_article_text
from train_cypher import examples

st.set_page_config(layout="wide")

st.title("ImpactGPT")


params = st.experimental_get_query_params()
context = f' My organisation has the follow attributes {params}. if i mention schemes or organizations or say something like "for me" or "my business" please use this attribute info. '
warning = ' If it does not seem like i am asking about schemes, proof points, claims or anything sustainability or business related, please do not attempt to write a cypher query and just respond normally. '
# st.info(context)

openai.api_key = os.environ.get('OPENAI_KEY')


def generate_response(prompt, cypher=True):
    if cypher and ('scheme' in prompt.lower() or 'proof point' in prompt.lower()):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=examples + "\n#" +
            # TODO: include user/account/org context into training
            # +  context + "\n#"
            prompt + "\n#" + warning,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        cypher_query = completions.choices[0].text
        if 'MATCH' not in cypher_query:
            return cypher_query, ''
        else:
            message = read_query(cypher_query)
            return message, cypher_query
    elif 'integration' in prompt.lower():
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=integration_info + "\n#" + prompt + "\n#" + warning,
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message, None
    else:
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=context + "\n#" + prompt + "\n#" + warning,
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message, None


# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input(
        "Questions about the framework? Ask away!", "", key="input")
    return input_text


col1, col2 = st.columns([2, 1])


user_input = get_text()

with col2:
    another_placeholder = st.empty()
with col1:
    placeholder = st.empty()


if user_input:
    # Append '?' to user_input if not present
    if not user_input.endswith('?'):
        user_input += '?'
    # Summarize articles
    if "summar" in user_input.lower():
        article_title = user_input.split(":")[1].strip()
        article_text = get_article_text(article_title)
        if not article_text:
            st.session_state.past.append(user_input)
            st.session_state.generated.append(
                (["Couldn't find any text for the given article"], ""))
        else:
            output, cypher_query = generate_response(user_input, cypher=False)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(([output], cypher_query))
    # English2Cypher with GPT
    else:
        output, cypher_query = generate_response(user_input)
        # store the output
        st.session_state.past.append(user_input)
        st.session_state.generated.append((output, cypher_query))

# Message placeholder
with placeholder.container():
    if st.session_state['generated']:

        message(st.session_state['past'][-1],
                is_user=True, key=str(-1) + '_user')

        is_empty_response = not bool(st.session_state['generated'][-1][0])



        # Check if the output is a list or a string
        if isinstance(st.session_state['generated'][-1][0], list):
            for j, text in enumerate(st.session_state['generated'][-1][0]):
                message(text, key=str(-1) + str(j))
        else:
            if is_empty_response:
                message('No Data Found :/')
            message(st.session_state['generated'][-1][0], key='gpt_output')


# Generated Cypher statements
#with another_placeholder.container():
 #   if st.session_state['generated']:
  #      st.text_area("Generated Cypher statement",
   #                  st.session_state['generated'][-1][1], height=240)

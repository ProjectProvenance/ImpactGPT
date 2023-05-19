# ImpactGPT

The base code was forked from https://github.com/tomasonjo/NeoGPT-Explorer.

Info on this project can be found here: https://medium.com/neo4j/knowledge-graph-based-chatbot-with-gpt-3-and-neo4j-c4ebbd325ed

## Intro

An AI chatbot that takes user input and generates a query to return framework data.

User inputs relating to Proof Points, Schemes or Claims Data will prompt GPT-3 to generate
a cypher query.

The database will be queried and results returned.

Queries not relating to the framework will prompt GPT-3 for a response directly and is more unpredictable.

## How to Run

Run the following commands to start the services:


1. Create an `.env` file and input your OPENAI API KEY as shown in `env.example`

2. Start docker services

```
docker-compose up
```

3. Open localhost:8501 in your browser

## Example questions

What is the vegetarian proof point?

What is the evidence for the vegan proof point?

My company uses renewable energy, which proof points would i be eligible for?

All our products are recyclable, which proof points might I be eligible fo

## Data 

The app is connected to our neo4j knowledge graph instance currently containing scheme data. 

## Preprocessing

The information extraction pipeline was executed with Diffbot API: See `notebooks/Preprocess.ipynb`.

## Feedback

Please create an issue if you have any feedback!


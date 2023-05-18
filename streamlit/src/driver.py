from neo4j import GraphDatabase

host = 'neo4j+s://192f8733.databases.neo4j.io'
user = 'neo4j'
password = 'RPFv2sCWGNfZrb4sKQnDiqjecrcZnxHhLm-xZigwfrs'
driver = GraphDatabase.driver(host, auth=(user, password))


def read_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        response = [r.values()[0] for r in result]
        return response


def get_article_text(title):
    text = read_query(
        "MATCH (a:Article {webTitle:$title}) RETURN a.bodyContent as response", {'title': title})
    return text

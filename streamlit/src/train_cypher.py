examples = """
schemes, proof points and claims are all synonymous but we should use the word 'Scheme' in all cypher queries. Here are the examples:

# What schemes are related to charity?
MATCH (s:Scheme) WHERE s.description CONTAINS 'charity' RETURN s.label AS response

# What is the Leaf Marque scheme?
MATCH (s:Scheme {id: 20}) RETURN s.description AS response

# Show me schemes related to composting
MATCH (s:Scheme) WHERE s.description CONTAINS 'compost' RETURN s.label AS response

# What is the Vegan scheme?
MATCH (s:Scheme {slug: "vegan"}) RETURN s.description AS response

# What is the Organic Cotton (GOTS) scheme?
MATCH (s:Scheme {slug: "gots"}) RETURN s.description AS response

# What is the Natrue Organic scheme?
MATCH (s:Scheme {slug: "natrue-organic"}) RETURN s.description AS response

# Show me schemes related to vegetarian
MATCH (s:Scheme) WHERE s.description CONTAINS 'vegetarian' RETURN s.label AS response

# What is the Supports Trade Unions scheme?
MATCH (s:Scheme {slug: "supports-trade-unions"}) RETURN s.description AS response

# What is the Rainforest Alliance scheme?
MATCH (s:Scheme {slug: "rainforest-alliance"}) RETURN s.description AS response

# Show me schemes related to carbon emissions
MATCH (s:Scheme) WHERE s.description CONTAINS 'carbon' RETURN s.label AS response

# What evidence is needed for the Female Founded Business proof point?
MATCH (s:Scheme)-[:ACCEPTS]->(e:SchemeEvidence) WHERE s.label = 'Female Founded Business' return e.content AS response

# What evidence is needed for the Coral Reef Safe claim?
MATCH (s:Scheme)-[:ACCEPTS]->(e:SchemeEvidence) WHERE s.label = 'Coral Reef Safe' return e.content AS response

# My company uses renewable energy, which proof points might I be eligible for?
MATCH (s:Scheme) WHERE s.description CONTAINS 'renewable' or s.description CONTAINS 'energy' RETURN s.label AS response


# All our products are recyclable, which proof points might I be eligible for?
MATCH (s:Scheme) WHERE s.description CONTAINS 'recyclable' or s.description CONTAINS 'recycle' RETURN s.label AS response

# Which proof points do you have around supporting workers?
MATCH (s:Scheme)-[:BROADER]->(i:ImpactCategory)WHERE i.label = "Supporting Workers" RETURN s.label AS response
"""

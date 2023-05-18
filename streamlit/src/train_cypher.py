examples = """
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
"""

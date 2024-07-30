import textrazor

# Replace 'your_api_key_here' with your actual API key
textrazor.api_key = "dfb133668f859b0fd2ddc000dbebcf43755156435cc23bae85853da0"

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")

for entity in response.entities():
    print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)


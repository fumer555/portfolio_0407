import json
from openai import OpenAI
# from scipy.spatial.distance import cosine
import os
from set_env import set_env

set_env()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment variables.")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# Load the JSON file
with open('./symptom.json', 'r') as file:
    symptoms = json.load(file)

# Convert values to embeddings
symptom_embeddings = {}
for key, value in symptoms.items():
    response = client.embeddings.create(
        input=value,
        model="text-embedding-ada-002"
    )
    embedding = response.data[0].embedding
    symptom_embeddings[key] = embedding

# Save the embeddings to a new JSON file
with open('./symptom_embeddings.json', 'w') as file:
    json.dump(symptom_embeddings, file)
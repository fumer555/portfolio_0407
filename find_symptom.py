import json
from openai import OpenAI
import os
import math

# Custom implementation of cosine similarity
def cosine_similarity(vec1, vec2):
    """
    Compute the cosine similarity between two vectors.
    """
    # Compute the dot product
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    
    # Compute the magnitudes (Euclidean norms)
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vec1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vec2))
    
    # Avoid division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    # Compute cosine similarity
    return dot_product / (magnitude1 * magnitude2)

def find_most_relevant_symptom(query):
    """
    Find the most relevant symptom based on the query.
    """
    # Ensure the API key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    # Load the saved embeddings
    with open('./symptom_embeddings.json', 'r') as file:
        symptom_embeddings = json.load(file)
    
    # Convert the query to an embedding
    response = client.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    query_embedding = response.data[0].embedding
    
    # Calculate similarities using custom cosine_similarity function
    similarities = {key: cosine_similarity(query_embedding, embedding) for key, embedding in symptom_embeddings.items()}
    
    # Find the most relevant key
    most_relevant_key = max(similarities, key=similarities.get)
    
    # Load the original symptoms to get the corresponding value
    with open('./symptom.json', 'r') as file:
        symptoms = json.load(file)
    
    # Return the key and its corresponding value
    return most_relevant_key, symptoms[most_relevant_key]

# Example usage
if __name__ == "__main__":
    query = "I keep feeling like I've been here before."
    key, value = find_most_relevant_symptom(query)
    print(f"Key: {key}, Value: {value}")
from langchain.embeddings import init_embeddings
import numpy as np



#embeddings = embed_model.embed_documents(sentences)
#.embed_documents(sentences) is used instead of .encode(sentences) when model is online not using llm on local machine



#we calculate cosine similarity only to check how similar two statements are...



def cosine_similatity(a,b):
    return np.dot(a , b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_model = init_embeddings(
    model="text-embedding-all-minilm-l6-v2-embedding",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length = False
)

sentences = [
    "I like Artificial Intelligence",
    "Generative AI is magnificant",
    "World is amazing"
]

embeddings = embed_model.embed_documents(sentences)
for embedding in embeddings:
    print(f"Len = {len(embedding)} --> {embedding[:4]}")

print("similarity 1 & 2 = ", cosine_similatity(embeddings[0], embeddings[1]))
print("similarity 1 & 3 = ", cosine_similatity(embeddings[0], embeddings[2]))
    

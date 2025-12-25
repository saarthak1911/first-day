from sentence_transformers import SentenceTransformer
import numpy as np

def cosine_similarity (a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_models = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love football.",
    "Soccer is my favorite sports.",
    "Messi talks spanish."
]

embeddings = embed_models.encode(sentences)

for embed_vector in embeddings:
    print("Length : ",len(embed_vector  ) , "-->", embed_vector[:4])

print("Sentences 1 & 2 similarity:" , cosine_similarity(embeddings[0], embeddings[1]))
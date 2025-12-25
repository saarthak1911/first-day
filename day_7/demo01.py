
# cmd> pip install sentence-transformers torch

from sentence_transformers import SentenceTransformer
import numpy as np

def consine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = [
    "I love football.",
    "Soccer is my favorite sports.",
    "Messi talks spanish."
    ]


#embeddings = embed_model.encode(sentences)
#.embed_encode(sentences) is used when you are not using langchain(retrieve, vector)
# .embed_document(sentences) is used when you are using langchain with document
emebeddings = embed_model.encode(sentences)

for embed_vect in emebeddings:
    print("Len:", len(embed_vect), " --> ", embed_vect[:4])

print("Sentence 1 & 2 similarity:", consine_similarity(emebeddings[0], emebeddings[1]))
print("Sentence 1 & 3 similarity:", consine_similarity(emebeddings[0], emebeddings[2]))


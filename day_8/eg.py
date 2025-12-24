from langchain.embeddings import init_embeddings
import numpy as np

def cosine_similarty(a,b);
return np.dot(a,b) / (np.linalg.norm(a)) * (np.linalg.norm(b))

embed_models = init_embeddings(
    model = "text-embedding-nomic-embed-text-v1.5",
    provider ="oipenai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "not-needed",
    check_embedding_ctx_length = False
)

sentences = [ 
    "I like Artificial Intelligence",
    "Generative AI is magnificant",
    "World is amazing"
]

embeddings = embed_models.embed_documents(sentences)
for embeddings in
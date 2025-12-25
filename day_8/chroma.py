
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings



#embedding model using langchain embeddings
embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#chunking usinglangchain
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 200, chunk_overlap = 20)
 
# client = chromadb.Client(settingschromadb.settings(persist_directory = "./chroma_db"))


client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("resumes")


 #chromadb.Client isdefault in-memory store
collection = client.get_or_create_collection(name = "demo")
chunks = text_splitter.split_text(raw_text)
embeddings = embed_model.embed_documents(chunks)


#prepare metadata & ids
ids = [f"doc_{i}" for i in range (len(chunks))]
metadatas = [ {"source" : "example.txt" , "chunk_id" : i} for i in range (len(chunks))]

#add data to chromadb
collection.add(ids = ids, documents = chunks , embeddings = embeddings , metadatas = metadatas)
client.persist()

#READ similarity search

query = "sample query text"
query_embedding = embed_model.embed_query(query)



# n_results = 3  it gives top 3 similar results amoung all stored embeddings
results = collection.query(query_embedding =[ query_embedding] , n_results = 3)
#get top 3 results -- with similarity to given query embedding


#inspect results
for doc, meta in zip(results["document"][0] , results["metadatas"][0]):
    print (meta ,"-->" , doc)

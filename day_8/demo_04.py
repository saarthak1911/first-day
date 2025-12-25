import chromadb


# db = chromadb.Client(settings=chromadb.Settings(persistent_directory="./knowledge_base"))
# collection = db.get_or_create_collection("resumes")
# collection.add(ids=["resume_id"], embeddings=[], metadatas=[], documents=[])
# db.persist()
    

#Data exists only while the program is running
#When your script stops → all embeddings are lost
#persist makes the data permanent by storing it on disk



db = chromadb.PersistentClient(path="./knowledge_base")
collection = db.get_or_create_collection("resumes")
collection.add(
    ids=["resume_id"],
    embeddings=[], 
    metadatas=[], 
    documents=[] )

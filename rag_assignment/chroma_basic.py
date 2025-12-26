import chromadb

# Step 1: Create a Chroma client (database)
client = chromadb.Client()

# Step 2: Create a collection (like a table)
collection = client.create_collection(name="my_collection")

# Step 3: Add text documents
collection.add(
    documents=[
        "Python is a programming language",
        "AI is changing the world",
        "Chroma is a vector database"
    ],
    ids=["doc1", "doc2", "doc3"]
)

print("Documents added successfully!")
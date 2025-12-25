from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import init_embeddings

embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)

def load_pdf_resume(pdf_path):
    # 1. Load PDF pages
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # 2. Chunking happens HERE ⬅⬅⬅
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    chunks = text_splitter.split_documents(docs)

    # 3. Extract chunk texts & metadata
    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    return texts, metadatas

resume_path = "F:/git_1/resume/resume-003.pdf"
resume_chunks, resume_metadata = load_pdf_resume(resume_path)

print("Total chunks:", len(resume_chunks))
print(resume_chunks[0])

# 4. Generate embeddings (ONE embedding per chunk)
resume_embeddings = embed_model.embed_documents(resume_chunks)

print("Total embeddings:", len(resume_embeddings))
print(f"Embedding length: {len(resume_embeddings[0])}")
print(f"First 4 values: {resume_embeddings[0][:4]}")

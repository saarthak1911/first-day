from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings


#PyPDFLoader is a LangChain document loader used to read PDF files and convert them into text documents page-by-page.


embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)

def load_pdf_resume(pdf_path):

    #load pdf and extract text
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    resume_content = ""
    for page in docs:
        resume_content += page.page_content
    metadata = {
        "source": pdf_path,
        "page_count": len(docs)
    }
    return resume_content, metadata

resume_path = "F:/git_1/resume/resume-003.pdf"
resume_text, resume_info = load_pdf_resume(resume_path)
print(resume_info)
print(resume_text)

resume_embeddings = embed_model.embed_documents([resume_text])
for embedding in resume_embeddings:
    print(f"Len = {len(embedding)} --> {embedding[:4]}")
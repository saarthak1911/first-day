from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings
import os
import streamlit as st


from PyPDF2 import PdfReader
from langchain_core.documents import Document


llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)

def load_pdf_resume(pdf_path):
    reader = PdfReader(uploaded_file)
    documents = []
    i = 0  # page counter

    for page in reader.pages:
        text = page.extract_text()
        documents.append(
            Document(
                page_content=text,
                metadata={"page": i, "source": uploaded_file.name}
            )
        )
        i += 1  # increment page number
    # st.success(f"Loaded {len(documents)} pages")
    st.write(documents[0].page_content)
    metadata = {
        "source": pdf_path,
        "page_count": len(documents)
    }
    return documents[0].page_content, metadata



with st.sidebar:
    st.title("Resume GPT")
    mode = st.selectbox("Select Mode", ["Ask anything", "Upload Resume"])



if mode == "Ask anything":
    query = st.chat_input("Ask something...")
    if query:
        
        response = llm.invoke([{"role": "user", "content": query}])
        # st.write("user").write(query)
        st.write("User : ", query)
        st.write("Assistant : ",response.content)

elif mode == "Upload Resume":  
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        query = st.chat_input("Ask something...")

        resume_text, resume_info = load_pdf_resume(uploaded_file)
    

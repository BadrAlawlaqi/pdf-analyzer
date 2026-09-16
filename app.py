import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

# 1. Load environment variables
load_dotenv()

# 2. Retrieve API Key
api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

# 3. Configure Streamlit Page
st.set_page_config(page_title="Smart PDF Analyzer", page_icon="📄", layout="wide")

st.title("📄 Smart PDF Analyzer & Q&A")
st.write("Upload any PDF document and ask questions about its content powered by AI!")

# 4. Sidebar Configuration for File Upload
with st.sidebar:
    st.header("⚙️ Document Settings")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + "\n"
    return extracted_text

# 5. Main Application Logic
if uploaded_file is not None:
    # Extract text once and save to Session State
    if "pdf_text" not in st.session_state or st.session_state.get("file_name") != uploaded_file.name:
        with st.spinner("Extracting and processing PDF text..."):
            st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
            st.session_state.file_name = uploaded_file.name
        st.sidebar.success("File processed successfully!")

    st.info(f"📁 **Active File:** {uploaded_file.name}")
    
    # Input field for user question
    user_question = st.text_input("Enter your question regarding the document:")

    if st.button("Analyze & Answer"):
        if not api_key:
            st.error("GEMINI_API_KEY is not set. Please check your .env file or Streamlit Secrets.")
        elif not user_question.strip():
            st.warning("Please enter a question first!")
        else:
            with st.spinner("Thinking and generating response..."):
                try:
                    # Initialize Google GenAI client
                    client = genai.Client(api_key=api_key)

                    # Prompt engineering for accurate Q&A
                    prompt = f"""
You are an expert document analysis assistant.
Answer the user's question based ONLY on the provided document text below.
If the answer cannot be found in the document, clearly state that it is not available.

---
DOCUMENT TEXT:
{st.session_state.pdf_text}
---

USER QUESTION: {user_question}
"""
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt,
                    )

                    st.markdown("### 🤖 Answer:")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"An error occurred while connecting to AI: {e}")
else:
    st.info("👈 Please upload a PDF file from the sidebar to begin.")
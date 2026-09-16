# 📄 Smart PDF Analyzer & Q&A

An AI-powered web application built with **Streamlit** and **Google Gemini API** that allows users to upload PDF documents and ask questions about their content in real time.

---

## 🌟 Features

- **PDF Text Extraction:** Reads and extracts text content from PDF documents seamlessly.
- **Context-Aware Q&A:** Answers user queries strictly based on the extracted content from the document.
- **Multi-lingual Support:** Responds in any requested language (English, Russian, Arabic, etc.).
- **Optimized Performance:** Utilizes Streamlit's `session_state` to avoid unnecessary re-parsing of PDF files.
- **Clean UI:** Simple, dark-themed, interactive user interface.

---

## 🛠️ Tech Stack

- **Frontend & UI:** [Streamlit](https://streamlit.io/)
- **AI Model:** [Google Gemini API](https://ai.google.dev/) (`gemini-3.6-flash`) via `google-genai` SDK
- **PDF Processing:** `pypdf`
- **Environment Management:** `python-dotenv`

---

## 🚀 Getting Started Locally

### Prerequisites

- Python 3.9 or higher
- A Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/BadrAlawlaqi/pdf-analyzer.git](https://github.com/BadrAlawlaqi/pdf-analyzer.git)
   cd pdf-analyzer

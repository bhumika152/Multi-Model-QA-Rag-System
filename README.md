📄 Enterprise Multi-Model Document Q&A System

A multi-model question-answering system designed to process and analyze various document types. Users can upload documents in multiple formats, which are then ingested and processed to provide answers to queries.

The project leverages LlamaIndex, Gemini, and HuggingFace Transformers for document processing and Q&A.

🚀 Overview

Upload documents in different formats.

Automatically parse, embed, and index data.

Ask questions and retrieve answers from document content.

Multi-model support for embeddings and QA.

🏗️ Architecture

Project Structure:

app.py → Main application logic. Handles UI, document upload, and query routing.

data_ingestion.py → Validates and loads files. Uses LlamaIndex.SimpleDirectoryReader.

embedding.py → Generates embeddings using HuggingFace or Gemini. Powers semantic search.

exception.py → Custom exceptions for robust error handling.

logger.py → Configures logging for debugging and monitoring.

setup.py → Helper functions used across modules.

⚙️ Installation

Clone the repository:

git clone <repository-url>
cd Multi-Model-QA-Rag-System


Install dependencies:

pip install -r requirements.txt

▶️ Usage

Run the Streamlit app:

streamlit run StreamlitApp.py


Upload documents via the interface.

Ask questions based on the uploaded content.

Choose the model (LlamaIndex, Gemini, HuggingFace) for answer generation.

📂 Supported File Types

📑 PDF → .pdf

📝 Word → .doc, .docx

📊 Excel → .xls, .xlsx

📽️ PowerPoint → .ppt, .pptx

📧 Emails → .eml, .msg

📄 Text → .txt

📉 CSV → .csv

📝 Logging

Application events and errors are logged for monitoring and debugging.

🤝 Contributing

Contributions are welcome! 🎉

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit changes (git commit -m "Add feature")

Push to branch (git push origin feature-name)

Open a Pull Request

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

🙌 Acknowledgments

LlamaIndex

Gemini

HuggingFace

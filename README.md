Overview
QA System is a multi-model question-answering system designed to process and analyze various document types. Users can upload documents in multiple formats, which are then ingested and processed to provide answers to user queries. The project leverages LlamaIndex, Gemini, and HuggingFace Transformers for document processing and QA.

Architecture
app.py: Main application logic. Handles user interface, document upload, and routes queries to the appropriate model (LlamaIndex, Gemini, HuggingFace).
data_ingestion.py: Validates and loads files. Uses LlamaIndex SimpleDirectoryReader for document parsing.
embedding.py: Generates embeddings for documents using models from HuggingFace or Gemini. Embeddings are used for semantic search and retrieval.
exception.py: Defines custom exceptions for robust error handling.
logger.py: Configures logging for debugging and monitoring.
setup.py: Contains helper functions used across modules.
Installation
Clone the repository:

git clone <repository-url>
cd Multi-Model-QA-Rag-System
Install dependencies:

pip install -r requirements.txt
Usage
To run the application:

streamlit run StreamlitApp.py
Upload documents via the interface. Ask questions based on the content; answers are generated using the selected model.

Supported File Types
PDF (.pdf)
Word (.doc, .docx)
Excel (.xls, .xlsx)
PowerPoint (.ppt, .pptx)
Images (.jpg, .jpeg, .png)
Email (.eml, .msg)
Text (.txt)
CSV (.csv)
Logging
Application events and errors are logged for monitoring and debugging.

Contributing
Contributions are welcome! Fork the repository and submit a pull request.

License
MIT License. See LICENSE for details.

Acknowledgments
LlamaIndex
Gemini
HuggingFace

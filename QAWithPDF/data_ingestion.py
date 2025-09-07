import os
import tempfile
import sys
import shutil
from exception import customexception
from logger import logging
from llama_index.core import SimpleDirectoryReader

# Supported file extensions
VALID_EXTENSIONS = [
    ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".ppt", ".pptx",
    ".jpg", ".jpeg", ".png", ".eml", ".msg", ".txt", ".csv"
]


def load_data(uploaded_files, keep_files=False):
    """
    Load documents from one or more uploaded files.

    Args:
        uploaded_files: A single file object or a list of file objects/paths.
        keep_files (bool): If True, keeps temporary files instead of deleting them.

    Returns:
        list: A list of loaded documents.
    """
    try:
        # Normalize input (support single or multiple files)
        if not isinstance(uploaded_files, (list, tuple)):
            uploaded_files = [uploaded_files]

        all_documents = []
        temp_paths = []

        for uploaded_file in uploaded_files:
            logging.info(f"📂 Starting load for: {getattr(uploaded_file, 'name', str(uploaded_file))}")

            # Validate file type
            file_ext = os.path.splitext(getattr(uploaded_file, "name", str(uploaded_file)))[1].lower()
            if file_ext not in VALID_EXTENSIONS:
                raise ValueError(f"❌ Unsupported file type: {file_ext}. "
                                 f"Supported types: {', '.join(VALID_EXTENSIONS)}")

            # Create temporary file with the proper extension
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
                if hasattr(uploaded_file, 'read'):
                    # File-like object (Streamlit uploads, etc.)
                    shutil.copyfileobj(uploaded_file, tmp_file)
                else:
                    # File path given directly
                    with open(uploaded_file, 'rb') as f:
                        shutil.copyfileobj(f, tmp_file)

                tmp_file_path = tmp_file.name
                temp_paths.append(tmp_file_path)

            # Load with SimpleDirectoryReader
            loader = SimpleDirectoryReader(input_files=[tmp_file_path])
            documents = loader.load_data()
            all_documents.extend(documents)

            logging.info(f"✅ Completed load for: {getattr(uploaded_file, 'name', str(uploaded_file))}")

        # Cleanup temp files if not needed
        if not keep_files:
            for path in temp_paths:
                try:
                    os.unlink(path)
                except OSError as e:
                    logging.warning(f"⚠ Could not delete temp file {path}: {e}")

        logging.info("🎉 All documents loaded successfully")
        return all_documents

    except Exception as e:
        logging.error(f"Exception in data loading: {str(e)}")
        raise customexception(e, sys)

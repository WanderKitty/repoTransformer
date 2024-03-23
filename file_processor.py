# file_processor.py

import logging
import os

def process_file(file_path, file_type):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        processed_file = {
            "path": os.path.abspath(file_path),
            "type": file_type,
            "content": content
        }

        return processed_file

    except Exception as e:
        logging.error(f"Error processing file {file_path}: {str(e)}")
        return None
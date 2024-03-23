#!/usr/bin/env python3

import os
import json
import logging
import fnmatch
from file_processor import process_file

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_ignore_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            return config['ignore_dirs'], config['ignore_files']
    except FileNotFoundError:
        logging.warning(f"Ignore configuration file '{config_file}' not found. Using default values.")
        return [], []
    except KeyError as e:
        logging.warning(f"Invalid ignore configuration file format. Missing key: {e}")
        return [], []

def should_ignore(path, ignore_dirs, ignore_files):
    for pattern in ignore_dirs:
        if fnmatch.fnmatch(os.path.basename(path), pattern) or \
           any(fnmatch.fnmatch(dir_name, pattern) for dir_name in path.split(os.path.sep)):
            return True

    for pattern in ignore_files:
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True

    return False

def transform_repo(repo_path, output_path, ignore_config):
    ignore_dirs, ignore_files = load_ignore_config(ignore_config)
    repo_data = {"files": []}

    try:
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_dirs, ignore_files)]

            for file in files:
                file_path = os.path.join(root, file)
                if should_ignore(file_path, ignore_dirs, ignore_files):
                    logging.info(f"Ignoring file: {file_path}")
                    continue
                file_type = os.path.splitext(file)[1][1:]
                logging.info(f"Processing file: {file_path}")
                processed_file = process_file(file_path, file_type)
                if processed_file:
                    repo_data["files"].append(processed_file)

        with open(output_path, 'w') as output_file:
            json.dump(repo_data, output_file, indent=2)
            logging.info(f"Transformed repository saved to: {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Repository Transformer")
    parser.add_argument("repo_path", help="Path to the repository")
    parser.add_argument("output_path", help="Path to the output file")
    parser.add_argument("--ignore-config", default="ignore.json", help="Path to the ignore configuration file")
    args = parser.parse_args()

    transform_repo(args.repo_path, args.output_path, args.ignore_config)
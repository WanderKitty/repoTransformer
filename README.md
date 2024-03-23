# Repository Transformer

Repository Transformer is a Python script designed to simplify the process of consolidating code repositories. It processes files within a repository and generates a single JSON file containing the transformed repository data. This tool is ideal for developers looking to analyze, share, or integrate repository data more efficiently.

## Key Features

- **Comprehensive Processing**: Recursively processes all files in the repository directory and its subdirectories.
- **Data Integrity**: Retains the original content of each file without preprocessing, ensuring authenticity and reliability of data.
- **Configurable Ignoring**: Utilizes `ignore.json` to selectively ignore specified directories and files, focusing on relevant data.
- **Simplified Data Handling**: Generates a single JSON file with the transformed repository data, streamlining data analysis and integration tasks.

## Why Repository Transformer?

Repository Transformer addresses the need for a straightforward way to aggregate repository data into a single, manageable file. This is particularly useful for:

- **Developers** looking to analyze their codebase for trends or inconsistencies.
- **Teams** aiming to share repository insights easily without navigating complex directory structures.
- **Integration** into other tools or systems, where a consolidated data format is required.

The output JSON file makes subsequent processing, analysis, or integration tasks more accessible by providing a structured and comprehensive dataset.

## Prerequisites

- Python 3.x installed on your system.

## Installation

To get started, clone the Repository Transformer to your local system:

```bash
git clone https://github.com/your-username/repoTransformer.git
```
## Usage

To get started, clone the Repository Transformer to your local system:

```bash
python repo_transformer.py [path-to-repository] [output-file.json] --ignore-config ignore.json


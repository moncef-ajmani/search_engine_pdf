# PDF Search Engine
This is a Python script that indexes the text content of PDF files in a directory and allows users to search for keywords within the content.

## Requirements
Python 3
PyPDF2
Whoosh
## Usage
Set the pdf_folder_path and index_folder_path variables in the script to the paths of the folder containing PDF files and the folder where the index will be stored, ## espectively.
Run the script in a terminal or command prompt by entering python pdf_search_engine.py.
The script will create an index of the PDF files in the specified folder and allow the user to search for keywords within the text content of the files.
Enter a search query when prompted and the script will display a list of the PDF files containing the query.
Note: If the index folder does not exist, it will be created automatically by the script.

## Acknowledgements
This script was created using the PyPDF2 library for extracting text from PDF files and the Whoosh library for indexing and searching the text content.

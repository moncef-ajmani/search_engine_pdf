import os
import PyPDF2
from whoosh.fields import *
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from whoosh import qparser

# Chemin vers le dossier contenant les fichiers PDF
pdf_folder_path = '...'

# Chemin vers le dossier où l'index sera stocké
index_folder_path = '...'

# Configuration des champs pour l'index
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

# Création de l'index
if not os.path.exists(index_folder_path):
    os.mkdir(index_folder_path)
ix = create_in(index_folder_path, schema)

# Ouvre chaque fichier PDF dans le dossier et extrait le texte
writer = ix.writer()
for filename in os.listdir(pdf_folder_path):
    if filename.endswith('.pdf'):
        filepath = os.path.join(pdf_folder_path, filename)
        with open(filepath, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            title = filename.split('.')[0]
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                content = page.extract_text()
                writer.add_document(title=title, path=filepath, content=content)
writer.commit()

# Recherche dans l'index
with ix.searcher() as searcher:
    query_str = 'model'
    print("Le mot :",query_str)
    print("Liste: ")
    query = QueryParser("content", ix.schema).parse(query_str)
    results = searcher.search(query, limit=None)
    links = []
    for hit in results:
        if(hit['title'] not in links):
            links.append(hit['title'])
            print(" - ",hit['title'])

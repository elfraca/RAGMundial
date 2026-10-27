from rag.document_loader import load_documents
from rag.text_splitter import split_documents

pages = load_documents()
chunks = split_documents(pages)

print(f"Se cargaron {len(pages)} páginas y se generaron {len(chunks)} fragmentos")
from langchain_community.document_loaders import PyPDFLoader

PDF_PATH = r"D:\Program Files (x86)\RAGProject\RAGMundial\data\raw\Mundial_2026.pdf"

def load_documents():
  loader = PyPDFLoader(PDF_PATH)
  return loader.load()

"""
for i, page in enumerate(pages):
  print(f"=== Pagina {i+1} ===")
  print(f"Contenido: {page.page_content}")
  print(f"Metadatos: {page.metadata}")
"""
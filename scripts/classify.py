import chromadb
from ollama import Client

# Load Ollama + Chroma
ollama = Client()
chroma = chromadb.PersistentClient(path="chroma_db")
taxonomy = chroma.get_collection("taxonomy")

# Document you want classified
doc_text = """
This document explains internal procedures for managing onboarding and workflows.
"""

# 1. Embed the document
emb = ollama.embeddings(
    model="nomic-embed-text",
    prompt=doc_text
)["embedding"]

# 2. Query nearest taxonomy categories
results = taxonomy.query(
    query_embeddings=[emb],
    n_results=3
)

print("Top category matches:")
for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    if "category" in meta:
        print(f"- {meta['category']} / {meta['subcategory']} → {doc}")
    else:
        print(f"- [DOCUMENT] → {doc}  (no taxonomy metadata)")


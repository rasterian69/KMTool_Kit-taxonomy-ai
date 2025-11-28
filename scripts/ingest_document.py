import chromadb
from ollama import Client

ollama = Client()
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Load the same taxonomy collection
collection = chroma_client.get_collection("taxonomy")

# Load a document (for now, just a string)
doc_text = """
This is a company policy that explains how employees should conduct themselves,
the ethical guidelines they must follow, and rules around confidentiality.
"""

# Create embedding
emb = ollama.embeddings(
    model="nomic-embed-text",
    prompt=doc_text
)["embedding"]

# Add to vector DB
collection.add(
    ids=["doc_1"],
    documents=[doc_text],
    embeddings=[emb],
    metadatas=[{"source": "example_doc"}]
)

print("Document ingested.")

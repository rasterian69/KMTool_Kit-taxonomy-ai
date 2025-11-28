import pandas as pd
import chromadb
from ollama import Client

# Load taxonomy
df = pd.read_csv("data/taxonomy.csv")

# Ollama client
ollama = Client()

# Chroma client
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Create collection
collection = chroma_client.create_collection(
    name="taxonomy",
    metadata={"hnsw:space": "cosine"}
)

# Create embeddings + add to Chroma
for idx, row in df.iterrows():
    text = f"{row['Category']} - {row['Subcategory']} - {row['Description']}"
    
    emb = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]

    collection.add(
        ids=[f"tax_{idx}"],
        documents=[text],
        embeddings=[emb],
        metadatas=[{
            "category": row["Category"],
            "subcategory": row["Subcategory"]
        }]
    )

print("Embeddings created and stored.")

# Test semantic search
query = "documents about how employees should act"
q_emb = ollama.embeddings(model="nomic-embed-text", prompt=query)["embedding"]

results = collection.query(
    query_embeddings=[q_emb],
    n_results=3
)

print("\nSearch results:")
for doc in results["documents"][0]:
    print("-", doc)

import chromadb
from ollama import Client

ollama = Client()
chroma = chromadb.PersistentClient(path="chroma_db")
taxonomy = chroma.get_collection("taxonomy")

# Document to classify
doc_text = """
This document explains internal procedures for managing onboarding and workflows.
"""

# 1. Embed and retrieve the top 5 taxonomy candidates
emb = ollama.embeddings(
    model="nomic-embed-text",
    prompt=doc_text
)["embedding"]

results = taxonomy.query(
    query_embeddings=[emb],
    n_results=5
)

# Build a taxonomy list for the LLM
taxonomy_candidates = []
for meta in results["metadatas"][0]:
    if "category" in meta:
        taxonomy_candidates.append(f"{meta['category']} → {meta['subcategory']}")

taxonomy_text = "\n".join(taxonomy_candidates)

# 2. LLM reasoning classification
prompt = f"""
Document:
\"\"\"
{doc_text}
\"\"\"

Possible taxonomy matches:
{taxonomy_text}

Choose the best category and subcategory from the list.
Return your answer in this format:

Category: <category>
Subcategory: <subcategory>
Reason: <short explanation>
"""

llm_response = ollama.generate(
    model="llama3.1",
    prompt=prompt
)

print(llm_response["response"])

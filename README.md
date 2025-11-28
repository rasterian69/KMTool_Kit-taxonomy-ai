# AI-Enhanced Knowledge Taxonomy Classifier

This project builds an **AI-powered document classification system**.  
Given a knowledge taxonomy and a folder of documents (PDF, DOCX, TXT), the tool automatically assigns each document to the **most relevant taxonomy category and subcategory** and outputs the results as a CSV file.

All processing runs **locally** using **Ollama** and **ChromaDB**.

---

## What the Tool Does

- Loads a taxonomy from `data/taxonomy.csv`
- Generates vector embeddings for each taxonomy entry
- Stores the taxonomy in a local vector database (ChromaDB)
- Reads documents from a folder (`documents/`)
- Extracts text from PDF, DOCX, and TXT files
- Splits large documents into chunks
- Generates embeddings using a local LLM embedding model (`nomic-embed-text`)
- Finds the closest taxonomy category using semantic similarity
- Outputs all classifications into `classification_results.csv`

---

## How It Works

### 1. build_taxonomy.py
- Reads the taxonomy CSV  
- Creates embeddings using `nomic-embed-text`  
- Stores them in a persistent ChromaDB collection called `taxonomy`

### 2. ingest_document.py
- Demonstrates ingesting a single example document  
- Embeds and stores the example in ChromaDB  

### 3. batch_classify.py
- Reads all files from the `documents/` folder  
- Extracts text using `extract_text.py`  
- Splits long documents into chunks  
- Embeds each chunk and averages the embeddings  
- Queries ChromaDB for the closest taxonomy entry  
- Writes the final results to `classification_results.csv`

---

## Installation

### 1. Enter the project directory
```
cd KMTool_Kit-taxonomy-ai
```

### 2. Create and activate a virtual environment
```
python3 -m venv ai-taxonomy-env
source ai-taxonomy-env/bin/activate
```

### 3. Install dependencies
```
pip install pandas chromadb ollama python-docx PyPDF2
```

### 4. Pull the embedding model for Ollama
```
ollama pull nomic-embed-text
```

---

## Project Structure

```
data/
    taxonomy.csv

scripts/
    build_taxonomy.py
    ingest_document.py
    extract_text.py
    batch_classify.py

documents/
    (put your PDFs, DOCX, and TXT files here)

chroma_db/
    (auto-created persistent vector database)
```

---

## How To Run The System

### 1. Build or rebuild the taxonomy
Run this whenever you update your taxonomy CSV:

```
python3 scripts/build_taxonomy.py
```

Expected output:

```
Loaded taxonomy
Embeddings created and stored.
```

---

### 2. Add documents to classify

Place your files inside:

```
documents/
```

Supported formats:
- `.pdf`
- `.docx`
- `.txt`

---

### 3. Run the batch classifier

```
python3 scripts/batch_classify.py
```

This will create:

```
classification_results.csv
```

Example results:

| file | category | subcategory |
|------|----------|-------------|
| HR_Policy.pdf | Content Types | Policies |
| Onboarding.docx | KM Processes | Capture |
| Workflow.txt | Content Types | Procedures |

---

## Done

You now have a fully local, private, AI-enhanced document classification system powered by:

- **Ollama**
- **ChromaDB**
- **Python**
- **Your custom Knowledge Taxonomy**

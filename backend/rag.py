import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge"
)

def search(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)
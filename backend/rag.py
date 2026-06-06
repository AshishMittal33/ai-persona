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

    return {
        "documents": results["documents"][0],
        "ids": results["ids"][0]
    }
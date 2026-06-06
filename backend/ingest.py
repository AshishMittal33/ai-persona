from knowledge import load_knowledge
from rag import collection

# Clear old data
try:
    collection.delete(ids=["knowledge"])
except:
    pass

text = load_knowledge()

# Split into chunks
chunk_size = 1000

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

for index, chunk in enumerate(chunks):

    collection.add(
        documents=[chunk],
        ids=[f"chunk_{index}"]
    )

print(f"Added {len(chunks)} chunks")
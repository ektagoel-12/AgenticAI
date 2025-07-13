import chromadb
client = chromadb.Client()
collection= client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This document is about New York",
        "This document is about Delhi"
    ],
    ids=['id1','id2']
)

all_docs=collection.get()
# print(all_docs)


documents=collection.get(ids=['id1'])
# print(documents)

results=collection.query(
    query_texts=['Query is about Chole Bhature'],
    n_results=2
)
print(results)

collection.delete(ids=all_docs['ids'])
collection.get()

collection.add(
    documents=[
        "This document is about New York",
        "This document is about Delhi"
    ],
    ids=['id1','id2'],
    metadatas=[
        {"url": "en.wikipedia.org/wiki/New_York_City"},
        {"url": "https://en.wikipedia.org/wiki/New_Delhi"}
    ]
)

import faiss
from tiktoken import get_encoding

index = faiss.IndexFlatL2(512)

def check_duplicate(email_data):
    """Check if an email is a duplicate using embeddings."""
    encoding = get_encoding("cl100k_base")
    email_vector = encoding.encode(email_data["body"])

    if index.ntotal > 0:
        D, I = index.search([email_vector], k=1)
        if D[0][0] < 0.5:
            return True, "Duplicate detected based on semantic similarity."
    
    index.add([email_vector])
    return False, "No duplicate detected."

# import Qdrant client
from qdrant_client import QdrantClient

# create Qdrant connection
client = QdrantClient(

    # qdrant server host
    host="localhost",

    # qdrant server port
    port=6333
)

# create collection
def create_collection():

    # print confirmation
    print("Collection created")

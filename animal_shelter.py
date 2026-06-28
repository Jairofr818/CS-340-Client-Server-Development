from pymongo import MongoClient


class AnimalShelter:
    """CRUD operations for the aac animals collection in MongoDB."""

    def __init__(self, username, password):
        """Initialize connection to MongoDB using username and password."""

        # MongoDB connection
        self.client = MongoClient(
            f"mongodb://{username}:{password}@localhost:27017/aac"
        )

        # Database and collection
        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert a document into the animals collection."""

        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create error:", e)
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query, projection=None):
        """Read documents from the animals collection."""

        try:
            if query is None:
                query = {}

            results = self.collection.find(query, projection)
            return list(results)
        except Exception as e:
            print("Read error:", e)
            return []

    def update(self, query, new_values):
        """Update matching documents in the animals collection."""

        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print("Update error:", e)
            return 0

    def delete(self, query):
        """Delete matching documents from the animals collection."""

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Delete error:", e)
            return 0
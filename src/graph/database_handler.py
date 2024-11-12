from pymongo import MongoClient
from config.config import config

class DatabaseHandler:
    def __init__(self):
        self.client = MongoClient(config.DATABASE_URI)
        self.db = self.client["cybersec_graph"]

    def store_graph(self, graph_data):
        self.db.graph.insert_many(graph_data)

    def retrieve_graph(self):
        return list(self.db.graph.find())

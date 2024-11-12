import networkx as nx

class GraphBuilder:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, entity, attributes=None):
        self.graph.add_node(entity, **(attributes or {}))

    def add_edge(self, source, target, relationship):
        self.graph.add_edge(source, target, relationship=relationship)

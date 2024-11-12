from src.graph.graph_utils import GraphUtils

class GraphUpdate:
    def __init__(self):
        self.graph_utils = GraphUtils()

    def update_graph(self, entities):
        for entity in entities:
            if not self.graph_utils.node_exists(entity):
                self.graph_utils.add_node(entity)
            else:
                self.graph_utils.update_node(entity)

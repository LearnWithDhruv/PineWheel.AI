class GraphUtils:
    def __init__(self, graph):
        self.graph = graph

    def node_exists(self, entity):
        return entity in self.graph.nodes

    def add_node(self, entity):
        self.graph.add_node(entity)

    def update_node(self, entity, attributes=None):
        for key, value in (attributes or {}).items():
            self.graph.nodes[entity][key] = value

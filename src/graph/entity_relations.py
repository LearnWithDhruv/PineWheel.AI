class EntityRelations:
    def __init__(self):
        self.entities = {}
        self.relationships = []

    def create_entity(self, entity_type, entity_id, attributes=None):
        if entity_id not in self.entities:
            self.entities[entity_id] = {
                "type": entity_type,
                "attributes": attributes or {}
            }
        return self.entities[entity_id]

    def add_relationship(self, source_id, target_id, relationship_type):
        relationship = {
            "source": source_id,
            "target": target_id,
            "type": relationship_type
        }
        if relationship not in self.relationships:
            self.relationships.append(relationship)

    def get_entities(self):
        return self.entities

    def get_relationships(self):
        return self.relationships

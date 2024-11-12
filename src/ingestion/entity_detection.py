class EntityDetection:
    def detect_entities(self, structured_text):
        entities = []
        for line in structured_text.splitlines():
            if "port" in line or "host" in line:
                entities.append(line)
        return entities

# memory.py
class MemoryStore:
    def __init__(self):
        self.memory = []

    def save(self, entry):
        self.memory.append(entry)

    def recent(self):
        return self.memory[-3:]

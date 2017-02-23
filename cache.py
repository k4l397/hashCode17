class Cache:
    def __init__(self, id):
        self.id = id
        self.latency = {}
        self.endpoints = {}
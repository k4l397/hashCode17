class Cache:
    Caches = {}
    NoOfCaches = 0
    Capacity = 0

    def __init__(self, id):
        self.id = id
        self.latency = {}
        self.endpoints = {}
        self.videos = []

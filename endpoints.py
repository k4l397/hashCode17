class Endpoint:
    Endpoints = []

    def __init__(self, id, latency):
        self.id = id
        self.datacenterLatency = latency
        self.latency = {}
        self.caches = {}
        self.videos = {}
        
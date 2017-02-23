class Endpoint:
    def __init__(self, id, latency):
        self.id = id
        self.datacenterLatency = latency
        self.caches = {}
        
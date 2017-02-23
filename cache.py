class Cache:
    Caches = {}
    NoOfCaches = 0
    Capacity = 0

    def __init__(self, id):
        self.id = id
        self.currentCapacity = 0
        self.latency = {}
        self.endpoints = {}
        self.videos = []
    
    def addVideo(self, video):
        self.videos.append(video.Id)
        self.currentCapacity += video.size

class Video:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.requests = []

    def setRequests(self, num, endpointID):
        newEntry = [endpointID, num]
        self.requests.append(newEntry)

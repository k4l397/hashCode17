class Video:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.requests = []
        self.totalRequests = 0

    def setRequests(self, num, endpointID):
        newEntry = [endpointID, num]
        self.requests.append(newEntry)
        self.totalRequests += newEntry[1]

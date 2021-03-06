import sys
from video import Video
from endpoints import Endpoint
from cache import Cache

def getInput(filename):
    f = open(filename, 'r')
    metadata = f.readline().strip()
    metadata = metadata.split(' ')
    noOfVideos = int(metadata[0])
    noOfEndpoints = int(metadata[1])
    noOfRequestDescriptors = int(metadata[2])
    noOfCacheServers = int(metadata[3])
    Cache.NoOfCaches = noOfCacheServers
    capacity = int(metadata[4])
    print 'Number of videos %d' % noOfVideos
    print 'Number of endpoints %d' % noOfEndpoints
    print 'Number of requests %d' % noOfRequestDescriptors
    print 'Number of cache servers %d' % noOfCacheServers
    print 'capacity of servers %d' % capacity

    Cache.Capacity = capacity

    sizes = f.readline().strip().split(' ')
    for x in range(0, noOfVideos):
        Video.Videos.append(Video(x, int(sizes[x])))

    i = 0
    while (i < noOfEndpoints):
        endpointData = f.readline().strip().split(" ")
        endpoint = Endpoint(i, int(endpointData[0]))
        for x in range(0, int(endpointData[1])):
            cacheData = f.readline().strip().split(" ")
            cacheId = int(cacheData[0])
            cacheLatency = int(cacheData[1])
            if Cache.Caches.has_key(cacheId):
                cache = caches[cacheId]
            else:
                cache = Cache(cacheId)
            cache.latency[endpoint.id] = cacheLatency
            cache.endpoints[endpoint.id] = endpoint
            endpoint.caches[cacheId] = cache
            endpoint.latency[cacheId] = cacheLatency
        Endpoint.Endpoints.append(endpoint)
        i += 1

    for line in f:
        if len(line.split(" ")) == 3:
            data = [int(x) for x in line.split(" ")]
            Video.Videos[data[0]].setRequests(data[2], data[1])
            Endpoint.Endpoints[data[1]].videos[data[0]] = data[2]
    f.close()

def sortVideos(videos):
    return sorted(videos, key = lambda x: x.totalRequests, reverse=True)

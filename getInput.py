import sys
from video import Video
from endpoints import Endpoint
from cache import Cache

if (len(sys.argv) < 2):
    print 'Require filename to use as command line argument'
    print 'eg: python getInput.py \'kittens.in\''
    sys.exit(1)
else:
    filename = sys.argv[1]

f = open(filename, 'r')
metadata = f.readline().strip()
metadata = metadata.split(' ')
noOfVideos = int(metadata[0])
noOfEndpoints = int(metadata[1])
noOfRequestDescriptors = int(metadata[2])
noOfCacheServers = int(metadata[3])
capacity = int(metadata[4])
print 'Number of videos %d' % noOfVideos
print 'Number of endpoints %d' % noOfEndpoints
print 'Number of requests %d' % noOfRequestDescriptors
print 'Number of cache servers %d' % noOfCacheServers
print 'capacity of servers %d' % capacity

videos = []
endpoints = []
caches = {}
sizes = f.readline().strip().split(' ')
for x in range(0, noOfVideos):
    videos.append(Video(x, int(sizes[x])))

i = 0
while (i < noOfEndpoints):
    endpointData = f.readline().strip().split(" ")
    endpoint = Endpoint(i, int(endpointData[0]))
    for x in range(0, int(endpointData[1])):
        cacheData = f.readline().strip().split(" ")
        cacheId = int(cacheData[0])
        cacheLatency = int(cacheData[1])
        if caches.has_key(cacheId):
            cache = caches[cacheId]
        else:
            cache = Cache(cacheId)
        cache.latency[endpoint.id] = cacheLatency
        cache.endpoints[endpoint.id] = endpoint
        endpoint.caches[cacheId] = cache
        endpoint.latency[cacheId] = cacheLatency
    endpoints.append(endpoint)
    i += 1

for line in f:
    if len(line.split(" ")) == 3:
        data = [int(x) for x in line.split(" ")]
        videos[data[0]].setRequests(data[2], data[1])
f.close()

print (videos[1].requests)
print (videos[1].totalRequests)

def sortVideos(videos):
    return sorted(videos, key = lambda x: x.totalRequests, reverse=True)

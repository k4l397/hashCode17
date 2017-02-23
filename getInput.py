import sys
from video import Video
from endpoint import Endpoint
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
    endpoint = Endpoint(i, endpointData[0])
    for x in range(0, endpointData[1]):
        cacheData = f.readline().strip().split(" ")
        if caches.has_key(cacheData[0]):
            caches[cacheData[0]].endpoints[endpoint] = cacheData[1]
        else:
            cache = Cache(cacheData[0])
            caches[cacheData[0]] = cache
            cache.endpoints[endpoint] = cacheData[1]
    endpoints.append(endpoint)
    i++

for line in f:
    if len(line.split(" ")) == 3:
        data = [int(x) for x in line.split(" ")]
        videos[data[0]].setRequests(data[2], data[1])
f.close()

print (videos[1].requests)
print (videos[1].totalRequests)

def sortVideos(videos):
    return sorted(videos, key = lambda x: x.totalRequests, reverse=True)

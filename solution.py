from cache import Cache
from endpoints import Endpoint
from video import Video
from getInput import getInput, sortVideos

if (len(sys.argv) < 2):
    print 'Require filename to use as command line argument'
    print 'eg: python getInput.py \'kittens.in\''
    sys.exit(1)
else:
    filename = sys.argv[1]

getInput(filename)

def fillCacheServer(cache, videos, endpoints):
    # sortedVids = sortVideos(videos)
    # cacheSize
    # for video in sortVideos:
    #     if (cacheSize + video.size) <= Cache.Capacity:
    #         cache.videos.append(video)

    for e in endpoints:
        for v in e.videos:
            for c in e.caches:
                i = v.requests[e.id]
                if (c.currentCapacity + v.size) <= c.capacity:
                    c.addVideo(v)






def solution(numberOfCacheServers, listOfaList):
    f = open("output.out", 'r')
    i = 0
    while i < numberOfCacheServers:
        line = str(i) + " ".join(listOfaList[i]) + "\n"
        print(line)
        f.write(line)

    f.close()

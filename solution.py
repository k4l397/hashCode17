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

def fillCacheServer(cache, videos):
    sortedVids = sortVideos(videos)
    cacheSize
    for video in sortVideos:
        if (cacheSize + video.size) <= Cache.Capacity:
            cache.videos.append(video)    

def solution(numberOfCacheServers, listOfaList):
    f = open("output.out", 'r')
    i = 0
    while i < numberOfCacheServers:
        line = str(i) + " ".join(listOfaList[i]) + "\n"
        print(line)
        f.write(line)

    f.close()

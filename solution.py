from cache import Cache
from endpoints import Endpoint
from video import Video

def fillCacheServer(cache):


def solution(numberOfCacheServers, listOfaList):
    f = open("output.out", 'r')
    i = 0
    while i < numberOfCacheServers:
        line = str(i) + " ".join(listOfaList[i]) + "\n"
        print(line)
        f.write(line)

    f.close()

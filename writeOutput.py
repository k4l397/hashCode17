from cache import Cache

def write():
    filename = 'output.out'
    f = open(filename, 'r')

    count = 0
    for cache in Cache.Caches:
        if (len(cache.videos) > 0) count += 1

    f.write('%d\n' % count)

    for i in range(0, Cache.NoOfCaches):
        videos = ''.join(str(x) for x in Cache.Caches[i].videos)
        f.write('%d %s\n' % Cache.Caches[i], videos)

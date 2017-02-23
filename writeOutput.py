from cache import Cache

filename = 'output.out'

f = open(filename, 'r')

count = 0
for cache in Cache.Caches:
    if (len(cache.videos) > 0) count += 1

f.write(count)

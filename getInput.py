from video import Video

file = open('kittens.in', 'r')
metadata = file.readline().strip()
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
sizes = file.readline().strip().split(' ')
for x in range(0, noOfVideos):
    videos.append(Video(x, int(sizes[x])))

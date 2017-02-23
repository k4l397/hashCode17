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
print noOfRequestDescriptors
print noOfCacheServers
print capacity 

videos = []
sizes = file.readline().strip().split(' ')
for x in range(0, noOfVideos):
    videos.append(Video(int(sizes[x])))

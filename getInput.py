from video import Video

file = open('me_at_the_zoo.in', 'r')
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

file.close()
f = open("me_at_the_zoo.in", "r")
for line in f:
    if len(line.split(" ")) == 3:
        data = [int(x) for x in line.split(" ")]
        videos[data[0]].setRequests(data[2], data[1])

# print (videos[1].requests)
# print (videos[1].totalRequests)

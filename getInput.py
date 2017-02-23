file = open('kittens.in', 'r')
metadata = file.readline().strip()
metadata = metadata.split(' ')
noOfVideos = metadata[0]
noOfEndpoints = metadata[1]
noOfRequestDescriptors = metadata[2]
noOfCacheServers = metadata[3]
capacity = metadata[4]
print 'Number of videos %s' % noOfVideos
print '' % noOfEndpoints
print noOfRequestDescriptors
print noOfCacheServers
print capacity  
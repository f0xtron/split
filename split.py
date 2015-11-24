#!/usr/bin/python
# Written by Brian Fox

import sys
print str(sys.argv)

start = sys.argv[1]
stop = sys.argv[2]
inputFile1 = sys.argv[3]
chunkSize1 = int(sys.argv[4])


def splitFile(start, stop, inputFile,chunkSize):

#read the contents of the file
	f = open(inputFile, 'rb')
	data = f.read() # read the entire content of the file
	f.close()

# get the length of data, ie size of the input file in bytes
	bytes = len(data)

#calculate the number of chunks to be created
	noOfChunks= bytes/chunkSize
	if(bytes%chunkSize):
		noOfChunks+=1
	if(stop == "max"):
		stop=bytes
	chunkNames = []
	for i in range(int(start), int(stop)+1, chunkSize):
		fn1 = inputFile + "_%s" % i
		chunkNames.append(fn1)
		f = open(fn1, 'wb')
		f.write(data[int(start):i+ chunkSize])
		f.close()
	print str(len(chunkNames)) + " files created"

splitFile(start, stop, inputFile1, chunkSize1)

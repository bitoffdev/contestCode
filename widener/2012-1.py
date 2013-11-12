#Completed in 5 minutes and 6 seconds on November 11, 2013
data = map(float, raw_input().split())
if data[2] > 12 :
	print (data[0]*1.05-data[1])/data[2]
else:
	print (data[0]-data[1])/data[2]
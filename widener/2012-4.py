#Completed in 18 minutes and 23 seconds on November 11, 2013
data = sorted(map(int, raw_input().split()))
data.reverse()
output = []
for z in range(len(data)):
	for y in range(z+1,len(data)):
		for x in range(y+1,len(data)):
			if pow(data[x], 2) + pow(data[y], 2) == pow(data[z], 2):
				output.append("(%d %d %d)" %(data[x], data[y], data[z]))
if len(output)>=1:
	output.reverse()
	print " ".join(output)
else:
	print "No Pythagorean triples found in the sequence."
#Completed in 12 minutes and 46 seconds on November 11, 2013
data = raw_input().split()
letters = "abcdefghijklmnopqrstuvwxyz".upper()
key = letters.find(data[1]) - letters.find(data[0])
if key < 0: key = 26 + key
output = ""
for char in data[2]:
	newcharindex = letters.find(char)-key
	if newcharindex < 0: newcharindex = 26 + newcharindex
	output += letters[newcharindex]
print output
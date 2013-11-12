#Completed in 5 minutes and 26 seconds on November 11, 2013
num = int(raw_input())
output = "YES"
for i in range(1,50):
	num = num + int(str(num)[::-1])
	if str(num)==str(num)[::-1]:
		output = "NO %d %d" %(i, num)
		break
print output
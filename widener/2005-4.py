from sys import stdin
import re
data = stdin.readline().split()
output = []
for item in data:
	text = list(re.match('\w*', item).group(0))
	punctuation = list(re.split('\w*', item))
	if len(text)>1:
		middle = text[1:-1]
		middle.reverse()
		output.append("".join(text[:1] + middle + text[-1:] + punctuation))
	else:
		output.append(item)
print " ".join(output)

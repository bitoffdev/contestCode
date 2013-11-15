#Google Code Jam 2012 Qualification Round
#Problem A. Speaking in Tongues
from sys import argv
script, infile, outfile = argv
data = [line.rstrip('\n') for line in open(infile)]
data.pop(0)
english= " abcdefghijklmnopqrstuvwxyz"
google = " ynficwlbkuomxsevzpdrjgthaq"
i = 1
output = open(outfile,"w")
for item in data:
        tempstr = ""
        for letter in item:
                tempstr+=english[google.find(letter)]
        output.write("Case #%d: %s\n" %(i, tempstr))
        i+=1

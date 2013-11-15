#Google Code Jam 2012 Qualification Round
#Problem B. Dancing With the Googlers
#from sys import argv
#filename = argv[0]
#data = open(filename).readlines()
data='''4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21'''.split("\n")
cases = data.pop(0)
for case in data:
    case = map(int, case.split())
    googlers = case.pop(0)
    surprising = case.pop(0)
    p = case.pop(0)
    totalpoints = case

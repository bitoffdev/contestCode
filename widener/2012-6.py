'''
This is my first attempt. It works okay, but not perfectly and sometimes gets a memory error.
'''
#Import itertools
import itertools
#Get input
totalrules = int(raw_input())
ruledata = raw_input().split()
start, target = raw_input().split()
#Create sequence of positions
sequence = []
for iternum in range(len(target)-1):
    sequence.append([])
    for posnum in range(iternum+1):
        sequence[iternum].append(posnum)
positions = list(itertools.product(*sequence))
#Create rules variable
rules = []
for i in range(0, len(ruledata), 2):
    rules.append([ruledata[i],ruledata[i+1]])
#Create sequence of possible rule indexes
ruleIndexes = [i for i in range(len(rules))]
iterRules = list(itertools.product(ruleIndexes, repeat=len(target)-1))
#Check for solution
iterations = []
solution = ""
for posSet in positions: #For each tuple of positions
    for ruleset in iterRules: #For each set of rules
        tempstr = start[0:]
        for i in range(len(posSet)):
            if rules[ruleset[i]][0] == tempstr[posSet[i]]:
                tempstr = tempstr[:posSet[i]] + rules[ruleset[i]][1] + tempstr[posSet[i]+1:]
            else:
                break
        if tempstr==target:
            solution = zip(ruleset, posSet)
print solution
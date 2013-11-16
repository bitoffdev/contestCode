heads, legs = map(float, raw_input().split())
cows = legs/2 - heads
chickens = -legs/2 + 2*heads
if chickens==int(chickens) and cows==int(cows):
    print "%d chickens %d cows" %(chickens, cows)
else:
    print "No Solution"

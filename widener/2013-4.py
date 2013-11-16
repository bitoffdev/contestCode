num = int(raw_input())
sequence = [num]
while True:
    num = sum([x*x for x in map(int,list(str(num)))])
    if num==1:
        print "YES, %d" %len(sequence)
	break
    elif num in sequence:
        print "NO, %d" %len(sequence)
	break
    sequence.append(num)

data = map(int, raw_input().split("-")[0].split())
numbers = []
for item in data:
    if item%2==0:
        numbers.append(float(str(item)[-1:]))
    else:
        numbers.append(float(str(item)[:1]))
print sum(numbers)/len(numbers)

price, discount, tax = map(float, raw_input().split())
print (price*(1-0.01*discount)) * (1+0.01*tax)

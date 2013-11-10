from sys import argv
script, balance, interest = argv
balance = int(balance)
interest = int(interest)
years = 0
while balance<1000000:
	balance += balance*interest*0.01
	years += 1
print years, "years"

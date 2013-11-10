#DEFINES VARIABLES:
tax = 6.5
items = ["Regular Hamburger", "Regular Cheeseburger", "Fish Sandwich", "Half-pounder with cheese", "French Fries", "Large Soft Drink"]
prices = [1.5, 1.75, 2.50, 2.75, 0.99, 1.25]
brline = "**********************************************************************"
#PRINTS MENU
print brline
print "McDowell's Restaurant"
print brline
print "Make your selection from the menu below:"
for i in range(0,6):
    print "%d. %s %f" %(i+1, items[i], prices[i])
print brline
#GETS INPUT AND PRINTS OUTPUT
data = int(raw_input("Select 1, 2, 3, 4, 5, or 6 ----->"))
print "Please pay %.2f dollars." % (prices[data-1]*(1+tax/100))
print "Thank you for eating at McDowell's!"

print("Welcome to My Pizzeria!")
name = input("What is your name? ")
print("Pizza Size(inches) Cost")
print("      10 $10.99")
print("      12 $12.99")
print("      14 $14.99")
print("      16 $16.99")
cost = 0
size = int(input("What size pizza do you want? Please enter a number: "))
if size == 10:
   cost = 10.99
elif size == 12:
   cost = 12.99
elif size == 14:
   cost = 14.99
elif size == 16:
   cost = 16.99
else:
   print("Sorry, I didn't understand you, so I will give you a 12 inch pizza.")
   size = 12
   cost = 12.99
print("All pizzas come with Cheese.")
toppings = 0
toppings_string = "Cheese "
answer = input("Do you want Pepperoni?")
if answer == "y" or answer == "Y":
   toppings += 1
   toppings_string += "Pepperoni "
answer = input("Do you want Sausage?")
if answer == "y" or answer == "Y":
   toppings += 1
   toppings_string += "Sausage "
cost += 1.25 * toppings
tax = round(cost * 0.0775, 2)   # use whatever your local Sales Tax rate is
final_cost = cost + tax
print (name + ", your order is as follows")
print (size, "-inch pizza")
print (toppings_string)
print ("The cost of your order is: $", cost)
print ("The sales tax is: $", tax)
print ("The total cost is: $", final_cost)
print ("Your order will be ready for pickup in 30 minutes.")
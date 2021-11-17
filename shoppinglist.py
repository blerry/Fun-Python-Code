# Add as many items in the shopping list as you want
mom_list = ["eggs", "milk", "butter", "bread", "flour"]
grocery_bag = []
print("STORE CLERK: Welcome to my grocery store.")
while True:
  answer = input("What item would you like to purchase? ")
  if answer == "check":
# display the shopping list
    print(grocery_bag)
  elif answer == "done":
    break 
  else:
    #  add the item to your shopping cart.
    if answer in mom_list:
      if answer in grocery_bag:
        print("CLERK: Sorry, you already purchased that time -- please try again")
      else:
        grocery_bag.append(answer)
    else:
      print("CLERK: I don't think that item is on your list -- please try again")
answer = input("MOM: Did you get everything on my list? ")
if len(grocery_bag) == len(mom_list):
  print("MOM: Thank you -- you got everything I wanted!!")
else:
  print("MOM: No - please try again...")
a=int(input("Ebter Your age:"))
print("Your age is:", a)
# condtional operators 
# >, <, >=, <=, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
# identation used for if else
if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You can't drive")
    print("No")
    print("Yeh")

# elif statement
applePrice = 20
budget = 200
if(budget - applePrice >50):
  print("Alexa, add 1 kg apples to the cart.")
elif(budget - applePrice > 70):
  print("Alexa, add 1 kg apples to the cart.")
else:
  print("Alexa, do not add apples to the cart.")

# another example
num=int(input("Enter the value of num:"))
if(num<0):
  print("Number is negative.")
elif(num == 0):
  print("Number is Zero.")
elif(num == 999):
  print("Number is special.")
else:
  print("Number is positive.")

print("i am happy now")

# Nested if else
num = 18
if(num<0):
  print("Number is negative.")  
elif(num>0):
  if(num<=10):
    print("Number is between 1-10")
  elif(num>10 and num<=20):
    print("Number is between 11-20")
else:
    print("Number is greater than 20")

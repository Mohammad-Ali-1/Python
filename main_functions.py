def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
      print("First number is greater")
    else:
      print("Second number is greater or equal")

def isLesser(a,b):
    pass
  

# Function are used to avoid code repetition, A function is a block of code that performs a specific task whenever it is called. built-in functions are already defined in python. user-defined functions are defined by the user.
a=9
b=8
isGreater(a,b)
# if(a>b):
#   print("First number is greater")
# else:
#   print("Second number is greater or equal")
calculateGmean(a,b)
# gmean=(a*b)/(a+b)
# print(gmean)
c=8
d=70
isGreater(c,d)
# if(c>d):
#   print("First number is greater")
# else:
#   print("Second number is greater or equal")
calculateGmean(c,d)
# gmean2=(c*d)/(c+d)
# print(gmean2)


# Function Arguments are the values that are sent to the function when it is called.
def Average(a=6,b=5):
    print("Average is",(a+b)/2)

Average(10,4)

def name(fname,mname="Jhon",lname="Whatson"):
    print("Hello,",fname,mname,lname)

name("Amy")

def average(*numbers):
  print(type(numbers))
  sum=0
  for i in numbers:
    sum=sum+i
    print("Average is:",sum/len(numbers))
    return 7

# return statement is used to return the value of the expression back to the calling function.

average(5,6,7,1)

# dictionary
def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Buchanan",lname="Barnes",fname="james")

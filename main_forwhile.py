#  Foor Loop
name="Mehemt Ibrahim"
for i in name:
    print(i)
    if i=="e":
        print("I found e")
        break

  # for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
     print(i)


# Range ()function
for k in range(5):
    print(k)
# it only print from 0 to 4
for k in range(1,11): 
    print(k)
  # it only print from 1 to 10
#  range (start,stop,step) function is used to generate a sequence of numbers.
for k in range(1,11,2):
    print(k)


# While Loop
print("while loop")
i=0 
while(i<10):
    print(i)
    i=i+1
i1=int(input("Enter a number"))
while(i1<=34):
    i1=int(input("Enter a number"))
    print(i1)
    # it will print the number until you enter a number greater than 100
print("Done")
  
count =5
while(count>0):
  print(count)
  count=count-1
else:
  print("I am inside else")


from collections.abc import ValuesView
import re


a=input("enter the number:")
print(f"multiplication table of {a} is:")
try:
  for i in range(1,11):
   print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
  print(e)
  print("sorry some error occured")
  print("Invalid input")
  # try and catch are used to handle the error,try block is used to run the code and catch block is used to handle the error
print("Some imp lines of code")
print("End of program")


try: 
  num=int(input("enter the number:"))
  a=[6,3]
  print(a[num])
except ValueError:
  # value error is used to handle the error when the input is not an integer
  print("number entered is not an integer")
except IndexError:
  # index error is used to handle the error when the input is not in the range of the list
  print("index error")

# finally block is used to run the code even if the error occurs

def fun1():
  try:
   l=[1,5,6,7]
   i=int(input("enter the index:"))
   print(l[i])
   return 1
  except:
   print("some error occured")
   return 0

  finally:
   print("i am always executed")

x=fun1()
print(x)

# finally is mostly used to close the file or to close the connection

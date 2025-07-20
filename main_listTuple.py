# list are used to store multiple items in a single variable and list can be changed
marks =[3,5,6,"Anamika",True,6,7,8,9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-3]) #negative index
print(marks[len(marks)-3])
print(marks[8-3])
print(marks[2])

if 7 in marks:
    print("Yes")
else:
    print("No")
if "arry" in "Harry":
    print("Yes")

print(marks)
print(marks[1:len(marks)-1])
print(marks[1:-1])
print(marks[0:8])
print(marks[0:8:2])

# list comprehension used to create new list from other iterables like list,tuple,dictionary,set,etc
lst=[i*i for i in range(10) if i%2==0]
print(lst)

# list methods are used to manipulate the list

list1=[1,2,3,4,5,2,2,4]
print(list1)
list1.append(7)
print(list1)
list1.sort(reverse=True)
print(list1)
list1.reverse()
print(list1.index(7))
# index() method is used to find the index of the first occurence of the specified value
print(list1.count(2))
list1.insert(1,899)
print(list1)
m=[900,1000,1100]
list1.extend(m)
print(list1)
# extend() method is used to add the elements of a list to the end of the current list
k=list1+m
print(k)


# Tuple are used to store multiple items in a single variable and tuple can not be changed
tup=(1,2,76,342,3,2,"green",True)
# tup[0]=90 we can't change the value of tuple
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[1:-2])

if 342 in tup:
    print("Yes")

tup1=tup[1:4]
print(tup1)

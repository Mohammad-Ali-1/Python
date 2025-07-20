# dictionary is nothing but key value pairs, it is unordered, unchangeable, do not allow duplicates
dic={
    "Harry":"Human being",
    "Spoon":"Object",
    344:"Integer",
    567:"Neha",
    
}
print(dic["Harry"])
print(dic[344])

info={"name":"Karan","age":19,"eligible":True}
print(info)
print(info["name"])
print(info.get("eligible"))
print(info.keys())
print(info.values())
# info.get is used to get the value of the key & it will not throw error if the key is not present in the dictionary
for key in info.keys():
    print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")


# Dictionary Methods
ep={122:45,123:89,"567":69,670:69}
ep2={222:67,566:90}
ep.update(ep2)
print(ep)
# ep.clear() # it will clear the dictionary
print(ep)
em={} # it will create an empty dictionary
print(em)
ep.pop(122)
print(ep)
ep.popitem() # it will remove the last item from the dictionary
print(ep)

del ep[123]
del ep["567"]
# del ep # it will delete the dictionary
print(ep)


# String can't be changed
a="Mehmet !!!! Mehmet !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("!"))
print(a.replace("Mehmet","Ali"))
print(a.split(" "))
blogHeading="introduction TO python"
print(blogHeading.capitalize())
str1="Welcome to the of the console!!!"
# center method aligns the string to the center as per the parameters given by the user
print(str1.center(100))
# count method returns the number of times the given value has occurred within the given string
print(a.count("Mehmet"))
# endswith() method checks if the string ends with a given value. If yes then return True, else return False.
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))
# find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
print(str1.find("to"))
print(str1.find("see"))
# index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
# print(str1.index("too"))
# isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str2="Welcome"
print(str2.isalnum())
# isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(str2.isalpha())

# islower() method returns True if all the characters in the string are lower case, else it returns False.
print(str2.islower())

# isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(str2.isprintable())

# isspace() method returns True only and only if the string contains white spaces, else returns False.
print(str1.isspace())

# istitle() method returns True if all the characters in the string are in title case, else it returns False.
print(str2.istitle())

# isstartwith() method checks if the string starts with a given value. If yes then return True, else return False.
print(str2.startswith("W"))

# swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
print(str2.swapcase())

# title() method capitalizes each letter of the word within the string.
print(str2.title())

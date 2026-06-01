# name = "Doremon"
# print(name)
# city = """Ahm"""
# print(city)
# print(name[0])
# print(name[-1])

# name[0] = "A" # Error
# print(name)

# print(name[0:4])
# print(name[2:])
# print(name[:6])
# print(name[:])
# print(name[0:5:2])
# print(name[::-1])
# print(name[-4:-1])
# print(name[-4:-1:1])
# print(name[-4:-1:2])

# print(name[3:-1])

# print(name.upper())
# print(name.lower())


# msg = "gOoD moRnIng"
# print(msg)

# print(msg.title())
# print(msg.capitalize())
# print(msg.swapcase())

"""
msg = "Good Morning"
print(msg.find("o", 3))
print(msg.find("w"))
print(msg.rfind("o", -11, -8))
print(msg.find("oo"))

print(msg.index("o", 3, 7))
print(msg.rindex("n", -8, -3))

print(msg.count("o"))
print(msg.count("1"))

print(msg.startswith("G"))
print(msg.startswith("Good"))
print(msg.startswith("G", 3))

print(msg.endswith("ing"))

"""


# msg2 = "   Namaste Duniya Namaste   "
# print(msg2)
# print(msg2.strip())
# print(msg2.lstrip())
# print(msg2.rstrip())
# print(msg2.replace("Namaste", "Hello"))


# text = "I am Programmer"
# print(text.split())

# email = "ansh@gmail.com"
# print(email.split("."))

# t = "a-b-c-d-e"
# print(t.rsplit("-", 2))

# t2 = "a\nb\nc"
# print(t2)
# print(t2.splitlines())


# print("-".join(["a", "b", "c"]))
# print("$".join(["a", "b", "c"]))
# print("\n".join(["a", "b", "c"]))


# check = "123abc"
# print(check.isalnum())
# check = "123abc$"
# print(check.isalnum())

# check = "abc"
# print(check.isalpha())

# check = "abc12"
# print(check.isalpha())

# check = "123"
# print(check.isdigit())
# check = "123A"
# print(check.isdigit())

# check = "12.3"
# print(check.isdigit())

# check = "⁷"
# print(check.isdigit())

# check = "123"
# print(check.isdecimal())

# check = "⁷"
# print(check.isdecimal())

# check = "⅔"
# print(check.isnumeric())

# check = "_no"
# print(check.isidentifier())
# check = "1no"
# print(check.isidentifier())

# check = "     "
# print(check.isspace())

# check = "  1   "
# print(check.isspace())

# check = "lower"
# print(check.islower())

# check = "Lower"
# print(check.islower())

# check = "UPPER"
# print(check.isupper())

# check = "Upper"
# print(check.isupper())

# check = "Hello World"
# print(check.istitle())

# check = "Hello world"
# print(check.istitle())


t = "Hi"
print(t.center(10, "-"))

print(t.ljust(10, "-"))
print(t.rjust(10, "-"))

no = "45"
print(no.zfill(5))

name = "Ram"
age = 21

print("My name is {} and age is {}".format(name, age))

print("Name : {name} | age : {age}".format_map({"name": "ansh", "age": 21}))

t = "Hello World"
print(len(t))

print(f"My name is {name} and age is {age}")

print("My name is %s and age is %d" % (name, age))

print('"Hello"')

print("\101")
print("\x4f")

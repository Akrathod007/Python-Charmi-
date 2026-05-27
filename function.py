# no return type and no arguments

"""
def sayHi():
    print("Hello")


sayHi()
sayHi()
sayHi()
sayHi()
sayHi()

"""

# no return type and with arguments

"""
def add(a, b):
    print(f"{a} + {b} = {a+b}")


n1 = int(input("Enter a number 1 : "))
n2 = int(input("Enter a number 2 : "))
add(n1, n2)

"""


# with return type and no arguments

"""
def mul():
    n1 = int(input("Enter a number 1 : "))
    n2 = int(input("Enter a number 2 : "))

    return n1 * n2


r = mul()
print(r)

print(mul())

"""


# with return type and with arguments


# def checkAlphabet(ch):
#     if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
#         return "Alphabet"
#     else:
#         return "Not an Alphabet"


# result = checkAlphabet("A")
# print(result)

# result = checkAlphabet("@")
# print(result)


"""
Create a Python program using:

Multiple functions
match-case
Menu driven program

The program should perform the following operations:

Palindrome Number
Armstrong Number
Strong Number
Perfect Number
Twin Number
Reverse Number

Take the user's choice and call the appropriate function using match-case.

"""

"""
def printList(li):
    for i in li:
        print(i)


def sumList(li):
    sum = 0
    for i in li:
        sum += i

    return sum


printList([1, 2, 3, 4, 5, 6])

sum = sumList([1, 2, 3, 4, 5, 6, 7])
print(sum)


def printTupel(li):
    for i in li:
        print(i)


printTupel((1, 2, 3, 4, 5))


def printDict(d):
    # for i in d:
    #     print(i, "->", d.get(i))
    for k, v in d.items():
        print(k, "->", v)


person = {"Name": "Ansh", "Age": 21, "City": "Ahm"}

printDict(person)


def squareList(li):
    squareLi = []
    for i in li:
        squareLi.append(i * i)

    return squareLi


print(squareList([1, 2, 3, 4, 5]))


def Math(a, b):

    return a + b, a - b, a * b, a / b


add, sub, mul, div = Math(20, 10)
print(add)
print(sub)
print(mul)
print(div)


print(Math(20, 10))

"""


# def add(a=30, b=20):
#     print("a:", a)
#     print("b:", b)
#     return a + b


# print(add(3, 5))
# print(add(4))
# print(add())

# print(add(b=20, a=100))


# def add(a, b, *args):
#     print(a)
#     print(b)
#     print(args)


# add(10, 20, 30, 40, 60, 70)


# def printList(*args):
#     print(args)


# li = [1, 2, 3, 4, 5]
# printList(*li)


# def hello(a, b, *args, **kargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kargs)


# hello(10, 20, name="Ram", age=21)


# def printDict(**kargs):
#     print(kargs)


# d = {"Name": "Ansh", "Age": 21}

# printDict(**d)

# greet = "Bye"


# def greet():
#     print("Hello")


# x = greet
# print(x())


def greet():
    print("Hello")


def call_func(func):
    func()


call_func(greet)


def outer():
    def inner():
        print("Inner function")
        return "Bye"

    return inner


f = outer

print(f()())


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


ops = [add, sub]

print(ops[0](10, 5))
print(ops[1](10, 5))


def outer():
    print("Outer function")
    x = 10

    def inner():
        nonlocal x
        y = 10
        x = x + 20
        print("Inner function")
        print(x)

    # print(y)

    inner()


outer()


x = 10


def change():
    global x
    x = x + 5
    print(x)


change()
print(x)

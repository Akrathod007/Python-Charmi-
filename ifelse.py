# no = int(input("Enter a number : "))

"""
if no > 0:
    print("Positive")
elif no < 0:
    print("Negetive")
else:
    print("Zero")
"""


"""
no - 4 ->  0100
1 ->       0001
&      ->  0000
"""
"""
if no & 1 == 0:
    print("Even")
else:
    print("Odd")

"""

"""
no = 10
no // 2 -> 5 * 2 = 10 == 10

no = 11

no // 2 -> 5 * 2 = 10 == 11
"""

# if no // 2 * 2 == no:
#     print("Even")
# else:
#     print("Odd")


# a = 10
# b = 20

# print("a :", a)
# print("b :", b)

"""
t = a
a = b
b = t
"""

"""
a = a + b
b = a - b
a = a - b
"""

# a = a + b - (b = a)
# print("a :", a)
# print("b :", b)


"""
amt = 1250
n500 - 2 
n100 - 2
n50 - 1
n20 - 0
n10 - 0
n5 - 0
n2 - 0
n1 - 0
"""

"""
amt = int(input("Enter a Amount : "))

n500 = n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

if amt >= 500:
    n500 = amt // 500  # 1250 // 500 -> 2
    amt = amt - n500 * 500
    # amt = 1250 - 2 * 500 => 1250 - 1000 = 250
if amt >= 100:
    n100 = amt // 100
    amt = amt - n100 * 100

if amt >= 50:
    n50 = amt // 50
    amt = amt - n50 * 50
if amt >= 20:
    n20 = amt // 100
    amt = amt - n20 * 20
if amt >= 10:
    n10 = amt // 10
    amt = amt - n10 * 10
if amt >= 5:
    n5 = amt // 5
    amt = amt - n5 * 5
if amt >= 2:
    n2 = amt // 2
    amt = amt - n2 * 2
if amt >= 1:
    n1 = amt // 1
    amt = amt - n1 * 1


print("Note500 :", n500)
print("Note100 :", n100)
print("Note50 :", n50)
print("Note20 :", n20)
print("Note10 :", n10)
print("Note5 :", n5)
print("Note2 :", n2)
print("Note1 :", n1)

"""


"""
no1 = int(input("Enter a number 1 :"))
no2 = int(input("Enter a number 2 :"))
no3 = int(input("Enter a number 3 :"))


if no1 == no2 == no3:
    print("All Numbers Are Equal")
elif no1 == no2 and no1 != no3:
    if no1 > no3:
        print("No1 and no2 are bigger than no3")
    else:
        print("No3 is bigger than no1 and no2")
elif no1 == no3 and no1 != no2:
    if no1 > no2:
        print("No1 and no3 are bigger than no2")
    else:
        print("No2 is bigger than no1 and no3")
elif no2 == no3 and no2 != no1:
    if no2 > no1:
        print("No2 and no3 are bigger than no1")
    else:
        print("No1 is bigger than no2 and no3")
elif no1 != no2 and no2 != no3 and no1 != no3:
    if no1 > no2:
        if no1 > no3:
            print("No1 is bigger")
        else:
            print("No3 is bigger")
    else:
        if no2 > no3:
            print("No2 is bigger")
        else:
            print("No3 is bigger")
"""

# x = 10
# y = 20

# result = "X is bigger" if x > y else "Y is bigger"
# print(result)

# a = 10
# b = 10

# print("A") if a > b else print("=") if a == b else print("B")


# if 5 > 2:
#     pass

"""
day = int(input("Enter a day between 1 to 7 : "))

match day:
    case 1:
        print("MON")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THU")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUN")
    case _:
        print("Wrong Day Number")
"""

# ch = input("Enter a character :")

# match ch:
#     case "A" | "E" | "O" | "I" | "U" | "a" | "e" | "o" | "i" | "u":
#         print("Vowel")


# print("1->Gujarati")
# print("2->South Indian")
# print("3->Punkabi")
# ch1 = int(input("Enter Your Choice : "))
# totalBill = 0
# match ch1:
#     case 1:
#         print("You Selected Gujarati")
#         print("1->Dhokla")
#         print("2->Thepla")
#         print("3->Dal Bhat")
#         ch2 = int(input("Enter Your Choice :"))
#         match ch2:
#             case 1:
#                 print("You Selected Dhokla")
#             case 2:
#                 print("You Selected Thepla")
#             case 3:
#                 print("You Selected Dal Bhat")
#         qty = int(input("How much do want?"))

#         if ch2 == 1:
#             totalBill = qty * 20
#         elif ch2 == 2:
#             totalBill = qty * 15
#         elif ch2 == 3:
#             totalBill = qty * 50
#     case 2:
#         print("You Selected South Indian")
#     case 3:
#         print("You Selected Punjabi")
#     case _:
#         print("Wrong Choice")


# print("Total Bill :", totalBill)


# no = int(input("Enter a number : "))

# match no % 2:
#     case 0:
#         print("Even")
#     case 1:
#         print("Odd")


# x = chr(65)
# print(x)

# x = ord("*")
# print(x)

"""
ch = input("Enter a character: ")
# ch = B
#   B >= 'A'
#   66 >= 65 and 65 <= 90
if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print("Alphabet")
elif ch >= "0" and ch <= "9":
    print("Digit")
else:
    print("Special")
"""


"""
ch = input("Enter a character: ")  # A

if ch in "AEIOUaeiou":
    print("Vowel")
elif (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print("Consonent")
elif ch >= "0" and ch <= "9":
    print("Digit")
else:
    print("Special")
"""


ch = input("Enter a character: ")  # A

if ch >= "A" and ch <= "Z":
    ch = ord(ch) + 32
elif ch >= "a" and ch <= "z":
    ch = ord(ch) - 32

print("Ch :", chr(ch))

# for i in range(1, 11):
#     print(i)


# i = 1
# sum = 0
# while i <= 10:
#     print(i)
#     sum = sum + i
#     i += 1

# print("Sum : ", sum)


"""
no = 458 -> 4 + 5 + 8 => 17

no = 458 // 10 -> 45
c++
no = 45 // 10 -> 4
c++
no = 4 // 10 -> 0
c++
"""

# n = int(input("Enter a number : "))
# c = 0
# while n > 0:
#     c += 1
#     n = n // 10

# print("Digit Count is", c)

# n = int(input("Enter a number : "))

# sum = 0
# mul = 1
# while n > 0:
#     d = n % 10
#     sum = sum + d
#     mul = mul * d
#     n = n // 10

# print("Digit Sum is", sum)
# print("Digit Product is", mul)

# # 123 -> 6

# if sum == mul:
#     print("Twin Number")
# else:
#     print("Not Twin Number")

# 1234 -> 1 + 4 = 5


# n = int(input("Enter a number : "))
# t = n
# rev = 0
# while n > 0:
#     d = n % 10
#     rev = rev * 10 + d
#     n = n // 10

# print("Reverse Number is", rev)

# if t == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


"""
1. krishnamurthy number : 

145 -> 1! + 4! + 5! -> 1 + 24 + 120 -> 145

2. Armstrong Number :

153 -> 1^3 + 5^3 + 3^3 -> 1 + 125 + 27 -> 153

1234 -> 
"""

# no = int(input("Enter a number : "))
# t = no
# t2 = no
# c = 0
# sum = 0
# while t > 0:
#     c += 1
#     t = t // 10

# print("Digit Count is", c)

# while t2 > 0:
#     d = t2 % 10
#     sum = sum + d**c
#     t2 = t2 // 10


# if sum == no:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")


# while True:
#     name = input("Enter a name or write x for exit : ")
#     if name == "x":
#         break
#     print("Name :", name)

"""
totalBill = 0

while True:
    print("1->Gujarati")
    print("2->South Indian")
    print("3->Punkabi")
    print("4 -> Exit")
    ch1 = int(input("Enter Your Choice : "))
    if ch1 == 4:
        break
    match ch1:
        case 1:
            print("You Selected Gujarati")
            print("1->Dhokla")
            print("2->Thepla")
            print("3->Dal Bhat")
            ch2 = int(input("Enter Your Choice :"))
            match ch2:
                case 1:
                    print("You Selected Dhokla")
                case 2:
                    print("You Selected Thepla")
                case 3:
                    print("You Selected Dal Bhat")
            qty = int(input("How much do want?"))

            if ch2 == 1:
                totalBill += qty * 20
            elif ch2 == 2:
                totalBill += qty * 15
            elif ch2 == 3:
                totalBill += qty * 50
        case 2:
            print("You Selected South Indian")
        case 3:
            print("You Selected Punjabi")
        case _:
            print("Wrong Choice")


print("Total Bill :", totalBill)
"""

"""
    1
   123
  12345
 1234567
123456789  
"""

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()

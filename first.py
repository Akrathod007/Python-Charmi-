# no = 10
# print(no)
# print(type(no))

# f = 3.14
# print(f)
# print(type(f))

# name = "Doremon"
# print(name)
# print(type(name))

# isActive = True
# print(isActive)
# print(type(isActive))

# n = None
# print(n)
# print(type(n))

# li = [1, 2, 3, 4, 5]
# print(li)
# print(type(li))

# t = (1, 2, 3, 4, 5)
# print(t)
# print(type(t))

# d = {"name": "Shinchan", "age": 2}
# print(d)
# print(type(d))

# s = {1, 2, 3, 4, 1, 2, 1}
# print(s)
# print(type(s))

# """

# """


# id, name, age = 1, "Ansh", 22
# print(id)
# print(name)
# print(age)


# city = input("Enter a City : ")
# print(city)

# no1 = int(input("Enter a number 1 :"))
# no2 = int(input("Enter a number 2 :"))

# # No1 : 10
# print("no1 :", no1)
# print("No2 : " + str(no1))
# print(no1 + no2)
# print(no1 - no2)
# print(no1 * no2)
# print(no1 / no2)  # 5/2 -> 2.5
# print(no1 // no2)  # 5/2 -> 2
# print(no1 % no2)
# print(no1**no2)


# == != > >= < <=

print("5 == 5 :", 5 == 5)
print("5 == 6 :", 5 == 6)
print("5 != 5 :", 5 != 5)
print("5 != 6 :", 5 != 6)
print("6 > 2 :", 6 > 2)
print("6 > 6 :", 6 > 6)
print("6 >= 6 :", 6 >= 6)
print("5 < 2 :", 5 < 2)
print("5 < 5 :", 5 < 5)
print("5 <= 5", 5 <= 5)

# Logical operator
# and or not

check = 5 > 2 and 6 < 3
print("and :", check)

check = 5 > 2 and 6 > 3
print("and :", check)

check = 5 > 2 or 6 > 3
print("and :", check)

check = 5 < 2 or 6 < 3
print("and :", check)

check = not (5 > 2)
print(check)

check = not (5 < 2)
print(check)


a = 10
b = 20
c = 15

check = not ((a < b and b > c and c > a) and (a == b or (a < b and c > a)))
print(check)


# no = 10

# no = no + 20
# no += 20

# bitwise operator
a = 5
b = 6

# 5 -> 0101
# 6 -> 0110
# ----------
# and  0011
print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a :", ~a)

"""
5 -> 0101
     1010
     
     1010
    
       1 
     0101 -> 1's Compliment
        1 -> 2's Compliment
    -----
     0110 -> -6
        
        
        0 + 1 = 1
        0 + 0 = 0
        1 + 0 = 1
        1 + 1 = 10
"""

print("5 << 1 :", 5 << 2)
print("5 >> 1 :", 5 >> 2)
# 5 -> 00000101
#  00000001
#      00010100 ->


# no1 > no2 ? no1 : no2

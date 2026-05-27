# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 3):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

"""
sum = 0
for i in range(1, 11):
    sum = sum + i

print("Sum is", sum)
"""

"""
5 * 1 = 5
5 * 2 = 10
"""

"""
no = int(input("Enter a number : "))

for i in range(1, 11):
    print(no, "*", i, "=", no * i)
"""

# 5! = 5 * 4 * 3 * 2 * 1
# no = int(input("Enter a number : "))
f = 1
# for i in range(no, 0, -1):
#     f = f * i

# for i in range(1, no + 1):
#     f = f * i

# print("F :", f)

"""
no = int(input("Enter a number : "))
f = 0

for i in range(1, no + 1):
    if no % i == 0:
        f += 1

if f == 2:
    print("Prime")
else:
    print("Not Prime")
"""


"""
    6 -> 6 % 2 == 0
"""

"""
no = int(input("Enter a number : "))

f = 1

for i in range(2, no):
    #  9 % 2 = 1
    # 9 % 3 = 0
    if no % i == 0:
        f = 0
        break

if f == 1:
    print("Prime")
else:
    print("Not Prime")
"""


# Perfect Number :
# 6 -> 1 2 3 -> 6

# for i in range(1, 11):
#     print(i, end=" ")


# 1 + 2 + 3 + 4 + 5 = 15

# print("Hello", end=" ")
# print("BYe")
# print("Again Hello")


# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)


# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

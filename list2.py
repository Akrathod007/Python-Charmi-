# li = [1, 2, 3, 4, 5, 6]

# i = 0

# while i < len(li):
#     print(li[i])
#     i += 1


# li = []

# while True:
#     name = input("Enter name or write x for exit : ")
#     if name.lower() == "x":
#         break
#     li.append(name)

# print(li)


l1 = [1, 2, 3, 4, 5]
l1[0:3] = [100, 200, 300]
print(l1)


a = [1, 2, 3, 4, 5]
# b = a
# b = a[:]

# b = list(a)

b = a.copy()
print(a)
print(b)

b[2] = 200
print(a)
print(b)

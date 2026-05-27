# li = [1, 2, 3, 4, 5]
# print(li)

# li2 = [1, True, 3.14, "Ram"]
# print(li2)

# li3 = [1, 2, 3, 1, 2, 5, 4, 3, 2]
# print(li3)

# print(li[3])
# print(li[-2])
# print(li3[0:6])
# print(li3[0:7:2])

# print(len(li3))

# print(sum(li3))


# li4 = [1, 1.4, 4, 5, 3, 7, 8, 3, 4]
# print(sum(li4))

# print(max(li4))
# print(min(li4))


# for i in li4:
#     print(i)

# for i in range(len(li4)):
#     print(li4[i], end=" ")

"""

1. Check each digit even or odd
1234
1->odd
2->even

2. Check each digit positive or zero

3. Check each digit is prime or not

no = 1234

1 is not prime
2 is prime
3 is prime
4 is not prime
"""

# li = [1, 2, 3, 4, [5, 6, [7, 9, 10], 8]]
# print(li)

# print(li[4][1])
# print(li[4][2][2])

# li = []
# print(li)

# li = list([1, 2, 3, 4])
# print(li)


# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# print(a * 3)

# a[2] = 300
# print(a)
# # print(a * b) #Error

# print(2 in a)
# print(4 not in a)


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)


l1 = [1, 2, 3, 4, 5]
print(l1)

l1.append(6)
print(l1)

l1.insert(2, 300)
print(l1)

l2 = [6, 7, 8]
l3 = [8, 9, 10]
l1.extend(l2)
l1.extend(l3)

print(l1)

print(l1.index(8))
# l1.reverse()
# print(l1)

l1.pop()
print(l1)

l1.pop(3)
print(l1)

# l1.pop(12)
# print(l1)

l1.remove(6)

print(l1)

# l1.remove(12)
# print(l1)

print(l1.count(8))

l4 = [1, 2, 3]
l4 = l1.copy()
print(l1)
print(l4)
l4[2] = 200

print(l1)
print(l4)

l1.clear()
print(l1)

# l1.pop()
del l1
print(l1)

t1 = ()
print(t1)
print(type(t1))
print(type(1))
li = [1, 2, [1, 2], [3, 4], [5, 6]]

i = 0
while i < len(li):
    if type(li[i]) == int:
        print(li[i])
    else:
        j = 0
        while j < len(li[i]):
            print(li[i][j])
            j += 1
    i += 1


# t2 = (1, 2, 3, 4)
# print(t2)

# t3 = (1, 3.14, "Ram", True)
# print(t3)

# t4 = 1, 2, 3, 4
# print(t4)
# print(type(t4))


# t5 = (1, 2, (3, 4), [1, 2, 4])
# print(t5)
# print(t5[1])
# print(type(t5[3]))
# t5[3].append(6)

# print(t5)


# t6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# #     0  1  2  3  4  5  6  7  8   9
# #                             -2  -1
# print(t6[2:])
# print(t6[2:-2])


# t7 = (10,)
# print(t7)
# print(type(t7))


# t1 = (1, 2, 3)
# t2 = (4, 5, 6)

# r = t1 + t2
# print(r)
# print(t1 * 3)

# print(3 in t1)
# print(4 in t1)
# print(3 not in t1)
# print(4 not in t1)

# print(len(t1))
# print(max(t1))
# print(min(t1))


# li = [1, 2, 3, 4, 5]

# t = tuple(li)
# print(t)

# t9 = (1, 2, 3, 1, 3, 2, 1, 1, 4, 1)
# print(t9.count(1))
# print(t9.index(1, 3, 7))


# t = 1, "Ram", 98
# print(t)

# roll, name, marks = t
# print(roll)
# print(name)
# print(marks)

# del t
# print(t)

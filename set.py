s = {}
print(s)
print(type(s))

s2 = {1, 2, 3, 4}
print(s2)
print(type(s2))

s3 = {1, 2, 3, 1, 1, 2, 3}
print(s3)


s4 = set()
print(s4)
print(type(s4))

s5 = set((1, 2, 3, 4))
print(s5)

# print(s5[0]) #Error

# s5 = {[1, 2, 3]}
# print(s5)

s5.add(6)
print(s5)

# s5.remove(3)
# s5.remove(33)

# s5.discard(3)
s5.discard(33)
print(s5)

s5.pop()
print(s5)

s5.clear()
print(s5)
# s6 = set()
# s6.pop()

li = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10]
# sum = 0
# for i in li:
#     sum = sum + i

# print("Sum :", sum)


# esum = 0
# osum = 0

# for i in li:
#     if i % 2 == 0:
#         esum += i
#     else:
#         osum += i

# print("Even Sum :", esum)
# print("Odd Sum :", osum)


# max = li[0]
# min = li[0]
# for i in li:

#     if max < i:
#         max = i

#     if min > i:
#         min = i

# print("Max :", max)
# print("Min :", min)

# l = li[0]
# sl = li[0]

# """
# 10 20 15

# """

# for i in li:
#     if i > l:
#         sl = l
#         l = i
#     elif i > sl and l != i:
#         sl = i

# print("Second Largest :", sl)

"""
1. Reverse a List Without Using reverse()

2. Remove Duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]

3. Find Common Elements Between Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

4. Flatten a Nested List
nested = [[1, 2], [3, 4], [5, 6]]

5. Remove All Even Numbers from a List
nums = [10, 15, 20, 25, 30, 35]

6. Find Elements Present in One List but Not in the Other
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

7. Check if a List is a Palindrome

8. Find All Unique Elements in a List
nums = [1, 2, 2, 3, 4, 4, 5]

9. Move All Zeros to the End
nums = [0, 1, 0, 2, 3, 0, 4]
"""

# 1. Reverse a List Without Using reverse()

# li = [1, 2, 3, 4, 5]

# rev = []

# for i in range(len(li) - 1, -1, -1):
#     rev.append(li[i])

# print("Rev :", rev)


"""
2. Remove Duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]
"""
# nums = [1, 2, 2, 3, 4, 4, 5]

# u = []

# for i in nums:
#     if i not in u:
#         u.append(i)

# print(u)


"""
3. Find Common Elements Between Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
"""
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# result = []

# for i in list1:
#     if i in list2:
#         result.append(i)

# print("Result :", result)


"""
4. Flatten a Nested List
nested = [[1, 2], [3, 4], [5, 6]]
"""

# nested = [[1, 2], [3, 4], [5, 6]]
# final = []

# for i in nested:
#     for j in i:
#         final.append(j)

# print("Final List :", final)


"""
6. Find Elements Present in One List but Not in the Other
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
"""

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# result = []

# for i in list1:
#     if i not in list2:
#         result.append(i)


# for i in list2:
#     if i not in list1:
#         result.append(i)

# print("Result : ", result)


# 7. Check if a List is a Palindrome

# li = [1, 2, 3, 2, 1]

# rev = []

# for i in range(len(li) - 1, -1, -1):
#     rev.append(li[i])

# print("Rev :", rev)

# if rev == li:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


"""
8. Find All Unique Elements in a List
nums = [1, 2, 2, 3, 4, 4, 5]
"""

# nums = [1, 2, 2, 3, 4, 4, 5]

# u = []

# for i in nums:
#     if nums.count(i) == 1:
#         u.append(i)

# print("Unique :", u)

"""
9. Move All Zeros to the End
nums = [0, 1, 0, 2, 3, 0, 4]
"""

# nums = [0, 1, 0, 2, 3, 0, 4]

# final = []

# for i in nums:
#     if i != 0:
#         final.append(i)

# len = nums.count(0)

# for i in range(len):
#     final.append(0)

# print("Final : ", final)


li = [3, 5, 7, 1, 2, 4, 6]
"""
    3, 5, 7, 1, 2, 4, 6

pass 1        : 3, 5, 7, 1, 2, 4, 6
    subpass1  : 3, 5, 7, 1, 2, 4, 6
    subpass2  : 3, 5, 7, 1, 2, 4, 6
    subpass3  : 3, 5, 1, 7, 2, 4, 6
    subpass4  : 3, 5, 1, 2, 7, 4, 6
    subpass5  : 3, 5, 1, 2, 4, 7, 6
    subpass6  : 3, 5, 1, 2, 4, 6, 7

"""


for i in range(len(li)):
    for j in range(len(li) - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]


print("Sorted Li :", li)

# square = []

# for i in range(1, 11):
#     square.append(i * i)

# print(square)

# square2 = [i * i for i in range(1, 11)]
# print(square2)


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_li = [i + 5 for i in li]
# print(new_li)

# even = []

# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# even2 = [i for i in range(1, 11) if i % 2 == 0]
# print(even2)


# evenOdd = []

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in li:
#     if i % 2 == 0:
#         evenOdd.append("Even")
#     else:
#         evenOdd.append("Odd")

# print(evenOdd)

# evenOdd2 = ["Even" if i % 2 == 0 else "Odd" for i in li]
# print(evenOdd2)


# marks = [90, 87, 96, 56, 78, 45, 70, 85]

# grade = [
#     "Grade A" if m >= 90 else "Grade B" if m >= 80 else "Grade C" if m >= 70 else "Fail"
#     for m in marks
# ]
# print(grade)


# no = int(input("Enter a number : "))

# li = []

# for i in range(1, no + 1):
#     li.append(int(input("Enter a n : ")))

# print(li)

# new_li = [int(input("Enter a n : ")) for i in range(1, no + 1)]
# print(new_li)

# row - 4 col - 3

"""
[
    [1,2,3],
    [4,5,6],
    [1,2,3],
    [4,5,6]
]
"""

# r = int(input("Enter a row : "))
# c = int(input("Enter a column : "))

# ol = []

# for i in range(1, r + 1):
#     il = []
#     for j in range(1, c + 1):
#         no = int(input("Enter a number : "))
#         il.append(no)
#     ol.append(il)

# print(ol)


# ol = [
#     [int(input("Enter a number : ")) for j in range(1, c + 1)] for i in range(1, r + 1)
# ]

# print(ol)


# s = {i * i for i in range(1, 10) if i % 2 == 0}
# print(s)


d = {i: i * i for i in range(1, 11)}
print(d)

ed = {i: i * i for i in range(1, 11) if i % 2 == 0}
print(ed)

evenOddDict = {i: (i * i if i % 2 == 0 else i**3) for i in range(1, 11)}
print(evenOddDict)


"""
Reverse word dictionary
words = ["python", "java", "c"]

ASCII value dictionary
s = "abcde"

Numbers divisible by 2 and 5
From 1 to 50 : key = number, value = "Yes" if divisible by both else skip   

Length filter (>3)
words = ["apple", "hi", "elephant", "go"]

Vowel frequency
s = "programming is fun"

Length square
words = ["cat", "tiger", "lion"]
"""

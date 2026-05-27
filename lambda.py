# add = lambda a, b: a + b

# print(add(2, 4))


# def evenOdd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# evenOdd2 = lambda n: "Even" if n % 2 == 0 else "Odd"

# print(evenOdd2(7))
# print(evenOdd2(78))


# check = lambda n: ("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

# print(check(10))
# print(check(-10))
# print(check(0))

# login = lambda user, pwd: (
#     "Admin Login"
#     if user == "admin" and pwd == "007"
#     else "User Login" if user == "user" and pwd == "xyz" else "Invalid Login"
# )

# print(login("admin", "007"))
# print(login("user", "xyz"))
# print(login("admin", "123"))


# nums = [1, 2, 3, 4, 5, 6, 7]

# s = list(map(lambda x: x * 2, nums))
# print(s)


"""
Create a list of numbers and use map() to find squares of all numbers.

Create a list of numbers and use map() to convert all numbers into strings.

Given a list of temperatures in Celsius, use map() to convert them into Fahrenheit.

Create a list of names and use map() to convert all names into uppercase.

Given a list of strings, use map() to find the length of each string.

Create a list of numbers and use map() to add 10 to every element.

Given a list of words, use map() to reverse each word.

Create a list of prices and use map() to add 18% GST to every price.

Create a list of integers and use map() to check whether each number is even or odd.
"""

nums = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, nums))
# even = list(filter(lambda x: True if x % 2 == 0 else False, nums))
# print(even)

from functools import reduce

# final = reduce(lambda a, b: a + b, nums)
# print(final)

# mul = reduce(lambda a, b: a * b, nums)
# print(mul)

# min = reduce(lambda a, b: a if a < b else b, nums)
# print(min)

# final = reduce(lambda a, b: a + b, nums, 10)
# print(final)


"""
Filter Task :

1. Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

2. Filter Odd Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

3. Filter Positive Numbers
numbers = [-5, 10, -2, 8, 0]

4. Filter Names Starting With A
names = ["Akshay", "Rahul", "Amit", "Karan"]

5. Filter Strings With Length More Than 5
words = ["apple", "banana", "kiwi", "mango"]

6. Filter Vowels From List
letters = ['a', 'b', 'e', 'f', 'i']

7. Filter Palindrome Words
words = ["madam", "python", "level", "code"]

8. Filter Uppercase Words
words = ["HELLO", "Python", "WORLD", "Code"]

9. Filter Alphabet Characters
data = ['A', '1', 'B', '9', 'C']

10. Filter Strings Containing Letter "a"
words = ["apple", "mango", "berry", "banana"]


Reduce Task :

1. Concatenate Strings
words = ["Python", "is", "awesome"]

2. Reverse a String
word = "python"

3. Find Total Digits in List
numbers = [123, 45, 6789]

4. Find Highest Marks
marks = [45, 78, 90, 66, 88]

5. Count Total Words Length
words = ["python", "java", "c"]




1. Square Even Numbers and Find Sum

2. Sum of Cubes of Positive Numbers

3. Find Sum of Squares of Odd Numbers

4. Find Largest Square of Even Numbers

5. Reverse Long Words and Join
Filter words whose length is greater than 4.

"""

# 1. Square Even Numbers and Find Sum
# l1 = [1, 2, 3, 4]

# final = reduce(
#     lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, l1))
# )

# print(final)

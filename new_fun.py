li = [True, True, False, True, False]

x = any(li)
print(x)

li = [False, False, False]
y = any(li)
print(y)

li = [0, 0, 0, 5]
z = any(li)
print(z)

t = (0, 0, 1224, 0)
y = any(t)
print(y)

s = {0, False}
x = any(s)
print(x)


marks = [25, 30, 35, 80]
result = any(mark >= 40 for mark in marks)
print(result)

t = (10, 50, 30, 40)
result = any(i > 30 for i in t)
print(result)

d = {"Maths": 90, "Science": 45, "Arts": 70}

result = any(m > 50 and m <= 70 for m in d.values())
print(result)

print("--------------------------------------------------------------------------")
nums = [True, True, True]
print(all(nums))


nums = [True, False, True]
print(all(nums))

nums = [10, 20, 30]
print(all(nums))

marks = [50, 60, 70, 80]
result = all(mark >= 40 for mark in marks)
print(result)

marks = [50, 60, 20, 80]
print(all(mark >= 40 for mark in marks))


print("--------------------------------------------------------------------------")

nums = [50, 10, 30, 20]
print(sorted(nums))
print(sorted(nums, reverse=True))


names = ["Raj", "Amit", "Kiran"]
print(sorted(names))

data = (5, 2, 8, 1)
print(sorted(data))

names = ["Python", "C", "Java", "JavaScript"]
print(sorted(names, key=len))

words = ["cat", "apple", "dog", "banana"]
print(sorted(words, key=lambda x: x[-1]))

nums = [-10, 5, -2, 8]
print(sorted(nums, key=abs))


student = {"name": "Raj", "age": 20, "city": "Ahmedabad"}

print(sorted(student))


people = [
    {"name": "Raj", "age": 25},
    {"name": "Amit", "age": 20},
    {"name": "Kiran", "age": 30},
]

result = sorted(people, key=lambda x: x["age"])
print(result)

students = [("Raj", 80), ("Amit", 60), ("Kiran", 90)]

# print(sorted(students, key=lambda x: x[1]))
x = sorted(students, key=lambda x: x[1])
print(students)
print(x)

li = [45, 34, 23, 67, 54]
li.sort()
print(li)

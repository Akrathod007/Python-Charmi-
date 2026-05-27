# person = {"name": "Ram", "age": 20}
# print(person)
# print(type(person))

# info = dict(name="Raju", age=21)
# print(info)

# print(info["name"])
# print(info.get("age"))
# print(info["city"])
# print(info.get("info"))

# del info["name"]

# val = info.pop("name")

# v = info.popitem()
# print(v)
# print(v[0])

# info.clear()
# print(info)

# employee = {"eid": 101, "ename": "Ram", "dsgn": "Manager", "salary": 20000}
# print(employee)


# for i in employee:
#     # print(i, "->", employee[i])
#     print(i, "->", employee.get(i))

# for i in employee.values():
#     print(i)

# for i in employee.keys():
#     print(i)

# for k, v in employee.items():
#     print(k, "->", v)


# # print(employee.get("city", "Ahm"))

# employee["city"] = "Surat"
# print(employee)

# employee.update({"salary": 30000, "state": "Guj"})
# print(employee)


# print(employee.pop("country", "India"))


# new_employee = employee.copy()
# print(new_employee)

# new_employee["city"] = "Ahm"
# print(employee)
# print(new_employee)


# li = ["Maths", "Science", "Arts"]

# d = dict.fromkeys(li, 0)
# print(d)


# employee.setdefault("Bonus", 20)

# print(employee)

# print(employee.setdefault("city"))

# print(len(employee))


# marks = {"Ram": {"Maths": 90, "Arts": 80}, "Shyam": {"Maths": 95, "Arts": 85}}

# print(marks)

# print(marks["Ram"]["Maths"])


# score_board = {"Virat": [90, 85, 70], "Sachin": [95, 45, 80], "Dhoni": [87, 65, 88]}

# total_score = 0
# for k, v in score_board.items():
#     print(k, "->", v)
#     sum = 0
#     for i in v:
#         sum += i
#     total_score += sum
#     print("Total Palyer Score :", sum)
# print("Total Score :", total_score)


# li = [1, 2, 3, 1, 2, 5, 6, 4, 3, 2, 1, 5, 6, 8]

# freq = {}

# for i in li:
#     freq.setdefault(i, li.count(i))

# print(freq)


# words = "apple banana banana apple mango kiwi kiwi"
# word = words.split()

# freq = {}
# print(word)

# for i in word:
#     freq.setdefault(i, word.count(i))

# print(freq)


# phonebook  = {}

while True:
    print("1-> Add phone")
    print("2-> Search phone by name")
    print("3->delete phone by name")
    print("4-> Exit")


"""
1. Remove Duplicate Values
d = {"a": 1, "b": 2, "c": 1, "d": 3}

2. Student Grade System
students = {"Ram": 85, "Shyam": 72, "Piya": 95}

3. Count Digits in Number
num = 1122334455
"""

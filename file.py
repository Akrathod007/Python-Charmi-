# f = open("Student.txt", "r")
# print(f.read())
# f.close()

# f = open("Student.txt", "w")
# f.write("Hello")
# f.close()

# f = open("Student.txt", "a")
# f.write("\nWorld")
# f.close()

# f = open("Student1.txt", "x")
# f.close()

# f = open("Student.txt", "r")
# data = f.read()
# data = f.read(10)
# print(data)
# print(f.readline())
# print(f.readline())
# data = f.readlines()
# print(data)
# f.close()

# f = open("Student.txt", "w")
# f.write("Hello\n")
# f.write("World\n")
# f.write("Bye\n")
# lines = ["Ram\n", "Shyam\n", "Mohan\n"]
# f.writelines(lines)
# f.close()

# with open("Student.txt", "r") as f:
#     data = f.read()
#     print(data)


# f = open("Student.txt", "r")
# print(f.tell())
# f.read(7)
# print(f.tell())
# f.close()


# import os

# if os.path.exists("Student1.txt"):
#     print("File Exists")
# else:
#     print("File Not Found")

# os.remove("student.txt")

# os.rename("Student1.txt", "Student.txt")

# f = open("Demo.txt", "w")
# f.write("Hello")
# f.close()

# try:
#     f = open("Demo.txt", "r")
#     print(f.read())

# except FileNotFoundError:
#     print("File Not Found")

# oldFile = open("Demo.txt", "r")
# data = oldFile.read()

# newFile = open("./File/NewFile.txt", "w")
# newFile = open("C:/Users/Ansh/Desktop/Hello.txt", "w")
# newFile.write("Hello")

# oldFile.close()
# newFile.close()

# f = open("image1.jpeg", "rb")
# data = f.read()
# print(data)
# f.close()

# f2 = open("bheem2.png", "wb")
# f2.write(data)

# f = open("audio2.mp3", "rb")
# data = f.read()
# print(data)
# f.close()

# f2 = open("song.mp3", "wb")
# f2.write(data)
# f2.close()

# f = open("employee.csv", "r")
# data = f.read()
# print(data)
# f.close()

# from PIL import Image

# img = Image.open("image1.jpeg")

# img.show()


vowel = "aeiouAEIOU"
count = 0
with open("example1.txt", "r") as f, open("Demo.txt", "w") as f2:
    for i in f:
        for j in i:
            if j not in vowel:
                count += 1
print(count)


with open("example1.txt", "r") as f:
    text = f.read()
    lines = text.splitlines()
    words = text.split()
    print("lines:", len(lines))
    print("words", len(words))
    print("chars", len(text))

name = "Doremon"

# for i in range(3, len(name)):
#     print(i, "->", name[i])

# for i in name:
#     print(i, end="")

# print()
# print(name[::-1])

rev = ""
# for i in range(len(name) - 1, -1, -1):
#     rev = rev + name[i]

# print(rev)

for i in name:
    rev = i + rev
    # rev = D + "" -> D
    # rev = o + D -> oD

print(rev)

if name == rev:
    print("Palindrome String")
else:
    print("Not Palindrome String")


"""
1. Count how many vowels are present in a string.

2. Count number of words in a string.

3. Convert lowercase to uppercase (without using upper())

4. Remove spaces from string

"""


name = "Shinchan"

print("".join(sorted(name)))

# anagram string
# listen -> silent

str1 = "Listen"
str2 = "silent"

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram String")
else:
    print("Not Anagram String")

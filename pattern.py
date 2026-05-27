# for i in range(1, 5):
#     for j in range(1, 5):
#         print("i :", i, "j :", j)


"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

A A A A A
B B B B B
C C C C C
D D D D D
E E E E E

A B C D E
A B C D E
A B C D E
A B C D E
A B C D E

"""
# ch = 65
# for i in range(1, 6):  # i - > 1
#     ch = 65
#     for j in range(1, 6):  # j-> 1 to 5
#         print(chr(ch), end=" ")
#         ch += 1
#     print()


# for i in range(65, 70):
#     for j in range(65, 70):
#         print(chr(j), end=" ")
#     print()


"""
* 
* *
* * *
* * * *
* * * * *

A
A B 
A B C 
A B C D
A B C D E
"""

# for i in range(1, 6):
#     ch = 65
#     for j in range(1, i + 1):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()


"""
1 2 3 4 5
1              1
0 1            2
1 0 1          3
0 1 0 1        4
1 0 1 0 1      5
"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")

#     print()


"""
1             # # * # #             *
A B           # # * # #             *
1 2 3         * * * * *         * * * * *
A B C D       # # * # #             *
1 2 3 4 5     # # * # #             * 
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 5 // 2 + 1 or j == 5 // 2 + 1:
#             print("*", end=" ")
#         else:
#             print("#", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 5 // 2 + 1 or j == 5 // 2 + 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


"""
*   *
 * *
  *
 * *
*   *


* * * * *
* * * *
* * *
* *
*
"""

# for i in range(1, 6):
#     for j in range(1, 6 - i + 1):
#         print("*", end=" ")
#     print()


"""
    *
   **
  ***
 ****
*****    

    *
   * *
  * * *
 * * * *
* * * * *   


    *
   ***
  *****
 *******
*********
    
"""
# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()


"""
    *
   ***
  *****
 *******
*********
"""
"""
s = 1

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, s + 1):
        print("*", end="")
    s += 2
    print()
"""


# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print("*", end="")
#     print()


"""
    1
   123
  12345
 1234567
123456789   


* * * * *
*       *
*       *
*       *
* * * * *


    *
   * *
  *   *
 *     *
*********
"""

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if i == 5 or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


"""
    1
   121
  12321
 1234321
123454321
"""

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
    
'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *    
'''



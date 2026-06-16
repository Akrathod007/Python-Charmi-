import time

print(time.time())

"""
start = 12345.23423
end =   12355.23423
"""


# start = time.time()

# for i in range(1000000):
#     pass

# end = time.time()

# print("Execution Time:", end - start)


# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)


# start = time.time()
# print(fibo(40))
# end = time.time()
# print("Execution Time:", end - start)


# d = {}


# def fibo(n):
#     if n in d:
#         return d[n]
#     elif n == 1:
#         d[1] = 1
#         return 1
#     elif n == 2:
#         d[2] = 1
#         return 1
#     else:
#         d[n] = fibo(n - 1) + fibo(n - 2)
#         return fibo(n - 1) + fibo(n - 2)


# start = time.time()
# print(fibo(40))
# end = time.time()
# print("Execution Time:", end - start)


# print("Start")
# time.sleep(3)
# print("End")


print(time.ctime())

print(time.ctime(100))

current = time.localtime()
print(current)

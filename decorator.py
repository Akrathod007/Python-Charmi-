# def decorator(func):
#     def wrapper():
#         print("Good Morning")
#         func()
#         print("Good Night")

#     return wrapper


# def display():
#     print("Hello")


# decorated = decorator(display)
# decorated()


# @decorator
# def sayHi():
#     print("Hiiii")


# sayHi()
# decorated = decorator(sayHi)
# decorated()


# def decorator_func(func):
#     def wrapper(*args, **kargs):
#         print("Before Function Call")
#         func(*args, **kargs)
#         print("After Function Call")

#     return wrapper


# def add(a, b):
#     print(a + b)


# decorated = decorator_func(add)
# decorated(10, 20)


# @decorator_func
# def mul(a, b, c):
#     print(a * b * c)


# mul(10, 20, 30)


# import time


# def timer_fun(func):
#     def wrapper(*args, **kargs):
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"{func.__name__} and time {end - start}")

#     return wrapper


# @timer_fun
# def loop1():
#     for i in range(1, 10):
#         time.sleep(1)
#         print(i)


# loop1()


def decorator_function(original_function):

    def wrapper(*args, **kwargs):

        result = original_function(*args, **kwargs)
        # print(result)
        return result

    return wrapper


@decorator_function
def add(a, b):
    return a + b


print(add(5, 3))


decorated = decorator_function(add)
decorated(10, 20)


def login_required(func):

    def wrapper():

        logged_in = True

        if logged_in:
            func()
        else:
            print("Please Login First")

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()


def loginRequired(func):
    def inner(*args, role):
        if role in args:
            print("authorized access:")
            func(args, role=role)
        else:
            print("unauthorized access:")

    return inner


@loginRequired
def accessHomePage(*args, role):
    print("accessing home page by", role)


accessHomePage("admin", "manager", "user", role="abcd")


@loginRequired
def accessCartPage(*args, role):
    print("accesing cart by", role)


accessCartPage("user", "admin", role="user")


def check(func):
    def inner(name, **kwargs):
        if len(kwargs) < 3:
            print("not all marks given")
            return
        else:
            func(name, **kwargs)

    return inner


@check
def grade(name, **kwargs):
    print("grade..")


grade("amit", maths=80, science=90, english=70)  # grade
grade("amit", maths=80)  # grade


def star(func):

    def wrapper():
        print("********")
        func()
        print("********")

    return wrapper


def hash_decorator(func):

    def wrapper():
        print("########")
        func()
        print("########")

    return wrapper


@star
@hash_decorator
def message():
    print("Hello")


message()

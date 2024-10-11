#todo define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#todo use these function as parameters in other functions
#functions are first class objects that means we can pass them as agruments

def calculate(calc_function, a, b):
    return calc_function(a, b)

#nested functions
#we can define a function in side a function

# def outer_func():
#     print("I am outer")
#
#     def i_am_inner():
#         print("I am Inner")
#
#     i_am_inner()
#

def outer_func():
    print("I am outer")

    def i_am_inner():
        print("I am Inner")

    return i_am_inner

#python decorater

#todo, create a smaple code

def decorater_func(function):
    def wrapper_function():
        function()
    return wrapper_function


@decorater_func
def say_hello():
    print("hello")


####################################################
import time

def delayed_decorater(functions):
    def wrapper_function():
        functions()
        print("running it again in 5 seconds.")
        time.sleep(5)
        functions()

    return wrapper_function()

# @delayed_decorater
# def hello_world():
#     print("hello_world")
####################################################

def decorater(function):
    def wrapper_function(x,y):
        a = function(x,y)
        b = function(y,x)
        return a == b
    return wrapper_function

def exponent(a,b):
    return a ** b

#checks id a raise to power b is equal to b raise to power a
check_symmetry = decorater(exponent)

print(check_symmetry(5,2))































# First-Calc
# My first Python Project - a calculator


import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


# Introduction and Instructions
print("Welcome to my Calculator")
print("It can perform all the basic operations and some advance ones too")
print("For Addition: +")
print("For subtraction: -")
print("For division: /")
print("For multiplication: *")
print("For percentage: %")
print("For exponents: **")
print("For square: sq")
print("For cube: cube")
print("For square root: sqrt")
print("For cube root: cbrt")
print("For quad: quad")
print("For quad root: quadrt")
print("For Absolute value: abs")
print("For reciprocal value: 1/")
print("For xth root: xrt")
print("For sin: sin")
print("For cos: cos")
print("For tan: tan")
print("For Compendo-Dividendo: CD")
print("For e^x: e")


# Code to run the programme
x = float(input("Enter First Number :"))
op =input("Enter op :")
y = float(input("Enter Second Number :"))

if op == "+":
    print(x+y)
elif op == "!":
    print(math.factorial(x))
elif op == "-":
    print(x-y)
elif op == "/":
    print(x/y)
elif op == "*":
    print(x*y)
elif op == "%":
    print((x/100)*y)
elif op == "**":
    print(x**y)
elif op == "sq":
    print(x**2)
elif op == "cube":
    print(x**3)
elif op == "sqrt":
    print(math.sqrt(x))
elif op == "cbrt":
    if x < 0:
        x = abs(x)
        print(x**(1/3)*(-1))
    else :
        print(x**(1/3))
elif op == "quad":
    print(x**4)
elif op == "quadrt":
    print(x**(1/4))
elif op == "abs":
    print(abs(x))
elif op == "1/":
    print(1/x)
elif op == "xrt":
    print(x**(1/y))
elif op == "sin":
    print(math.sin(x))
elif op == "cos":
    print(math.cos(x))
elif op == "tan":
    print(math.tan(x))
elif op == "CD":
    print((x+y)/(x-y))
elif op == "e":
    print(math.exp(x))
else:
    print("Invalid")

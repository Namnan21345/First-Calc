# First-Calc
My first Python Project - a calculator


import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

x = float(input("Enter x :"))
op =input("Enter op :")
y = float(input("Enter y :"))

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

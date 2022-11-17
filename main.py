from math import sqrt
import re

# Author: Rodrigo Tavares
# Date: 17/11/2022
# Title: Calculator
# Version: 1.4
# This program is a simple calculator that can calculate the square root of any integral number aswell as any other simple operations with integral or decimals
# If you want to use decimals use (.) and not (,)
print(f"Welcome to the python calculator\nType esc if you want to exit\n")

while 1:
    print(f"Insert your calculation:")
    calc = input()
    if calc == "esc":
        print("Goodbye!...")
        break
    elif re.search("\Asqrt\(\d+\)|((\d+)(\+|-|\/|\*))+(\d+)|\Aesc", calc):
        print(calc + " = " + str(eval(calc)))
    else:
        print(f"Invalid calculation, try again or write 'esc' to exit")

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:57:44 2021
@author: ramesh.kp
"""

print()
print("#" * 30)
def one():
    return 1

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def calculator(func, a, b):
    return func(a, b)

print(type(one))
print(calculator(add, 3, 5))
print(calculator(substract, 10, 4))
print("#" * 30)

#   Nested Functions
# Gallons to Cups
# 1 Gallon = 4 Quarts
# 1 Quart = 2 Pints
# 1 Pint = 2 Cups    
def convert_gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f"Converting {gallons} gallons to quarts !")
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f"Converting {quarts} quarts to pints !")
        return quarts * 2
    def pints_to_cups(pints):
        print(f"Converting {pints} pints to cups !")
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    return cups

print(convert_gallons_to_cups(1))
print(convert_gallons_to_cups(3))
print("#" * 30)

def calculator(operation):
    return_string = "Invalid Operation"
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def invalid(a, b):
        return return_string
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    else:
        return invalid

print(calculator("add")(10, 4))
print(calculator("subtract")(7, 7))
print(calculator("multiply")(10, 7))

def square(num):
    return num ** 2
def cube(num):
    return num ** 3
def times10(num):
    return num ** 10

operations = [square, cube, times10]
for func in operations:
    print(func(5))

print("#" * 30)
print()

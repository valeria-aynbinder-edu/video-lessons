import math
from decorators import *


@greeting_decorator
def factorial():
    num = int(input("Please insert a number: "))
    fact = math.factorial(num)
    print(f"The factorial of {num} is {fact}")


@greeting_decorator
def capitalize():
    txt = input("Please insert a text to capitalize: ")
    print(f"Your capitalized text is: {txt.capitalize()}")


@greeting_decorator
def convert_from_farenheit():
    temp_F = float(input("Please insert a temperature in °F: "))
    temp_C = (temp_F - 32) * (5/9)
    print(f"{temp_F} in °F is {temp_C} °C")


@greeting_decorator
def convert_from_celcius():
    temp_C = float(input("Please insert a temperature in °C: "))
    temp_F = (temp_C * (9/5)) + 32
    print(f"{temp_C} in °C is {temp_F} °F")

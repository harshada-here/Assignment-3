#ASSIGNMENT 3
#Task 1: Calculate Factorial Using a Function 

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is : {factorial(n)}")

#Task 2: Using the Math Module for Calculations
import math
num = float(input("Enter a number: "))
sq_rt = math.sqrt(num)
sine = math.sin(num)
logarithm = math.log(num)
print(f"Square root: {sq_rt}")
print(f"Logarithm: {logarithm}")
print(f"Sine: {sine}")
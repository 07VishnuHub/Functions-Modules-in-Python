Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

nunber = int(input("Enter a number to calculate its factorial: "))

result = factorial(nunber)
print(f"The factorial of {nunber} is {result}.")

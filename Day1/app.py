# 1. Print "Hello Python" to the console
print("Hello Python")

# 2. Perform addition, subtraction, multiplication, and division of two numbers input by the user
num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2 if num2 != 0 else 'Undefined (division by zero)'}")

# 3. Generate and print a random number between a specified range
import random
st = int(input("\nEnter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Random number between {st} and {end}: {random.randint(st, end)}")

# 4. Display the calendar of a given month and year
import calendar
year = int(input("\nEnter year: "))
month = int(input("Enter month (1-12): "))
print(calendar.month(year, month))

# 5. Check if a given year is a leap year
year = int(input("\nEnter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is {'a leap year' if is_leap else 'not a leap year'}.")

# 6. Print all prime numbers within a specified range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

st = int(input("\nEnter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {st} and {end} are:", end=" ")
for num in range(st, end + 1):
    if is_prime(num):
        print(num, end=" ")

# 7. Find the factorial of a number input by the user
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

number = int(input("\n\nEnter a number: "))
print(f"Factorial of {number} is {factorial(number)}")

# 8. Print the Fibonacci sequence up to a specified number of terms
n_terms = int(input("\nEnter the number of terms: "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:", end=" ")
while count < n_terms:
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2
    count += 1

# 9. Find all Armstrong numbers within a specified range
def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    return number == sum(int(digit) ** num_len for digit in num_str)

st = int(input("\n\nEnter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Armstrong numbers between {st} and {end} are:", end=" ")
for num in range(st, end + 1):
    if is_armstrong(num):
        print(num, end=" ")

# 10. Print the reverse of a string input by the user
user_string = input("\n\nEnter a string: ")
print(f"The reverse of '{user_string}' is '{user_string[::-1]}'")

# 11. Calculate and print the sum of the first ten natural numbers
print(f"\nThe sum of the first ten natural numbers is: {sum(range(1, 11))}")

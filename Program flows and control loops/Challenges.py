# Challenge 1
# Write a Python script that asks the user for a number and prints a list of all its divisors for each number less than the given number.

num = int(input("Enter a number: "))
divisors = []
for i in range(1, num):
    if num % i == 0:
        divisors.append(i)
print(f"The divisors of {num} are: {divisors}")

# Challenge 2

# Challenge #2
# Write a Python program to check if an integer x is a power of another integer y. Prompt the user to input both numbers.
# Input: 16, 2
# Output: 2 ** 4 = 16

x = int(input("Enter the number: "))
y = int(input("Enter the base: "))

power = 0
result = 1

while result < x:
    result *= y
    power += 1

if result == x:
    print(f"{y} ** {power} = {x}")
else:
    print(f"{x} is not a power of {y}")

# Challenge #3

# Write a Python program that counts and displays the vowels of a given string, ignoring the letter case.

# Input str: Hello Everybody!

# Output: 5
text = input("Enter a string: ")

count = 0

for letter in text:
    if letter.lower() in 'aeiou':
        count += 1

print(count)

# Challenge #4

# Write a Python script that checks whether a triangle is equilateral, isosceles, or scalene.
# Prompt the user to enter the lengths of the three sides.

# Triangle Types:

# Equilateral: All three sides are equal.

# Isosceles: Two sides are equal.

# Scalene: All sides are different.

# Input: Enter the lengths of the triangle sides:

# x: 6

# y: 8

# z: 12

# Output: Scalene triangle.
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle.")
elif x == y or y == z or x == z:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")

# Challenge #5

# Write a Python program that prompts the user for multiple float numbers and calculates:

# The sum

# The product

# The average

# Enter 0 to finish.
numbers = []

while True:
    num = float(input("Enter a number (0 to finish): "))
    if num == 0:
        break
    numbers.append(num)

if len(numbers) == 0:
    print("No numbers entered.")
else:
    total = sum(numbers)
    
    product = 1
    for num in numbers:
        product *= num
    
    average = total / len(numbers)

    print(f"Sum: {total}")
    print(f"Product: {product}")
    print(f"Average: {average}")

# Challenge #6

# Given a string, write a program that calculates the sum and average of all digits in the string, ignoring other characters.

# Example:

# Input: "Python31py50"

# Output: Sum: 9, Average: 2.25
text = input("Enter a string: ")

digits = []

for char in text:
    if char.isdigit():
        digits.append(int(char))

if len(digits) == 0:
    print("No digits found.")
else:
    total = sum(digits)
    average = total / len(digits)
    print(f"Sum: {total}, Average: {average}")

# Challenge #7

# Write a Python program that displays the multiplication table (from 1 to 10) for a number entered by the user.

# Input: User enters 8

# Output:

# 8 x 1 = 8

# 8 x 2 = 16

# 8 x 3 = 24

# 8 x 4 = 32

# 8 x 5 = 40

# 8 x 6 = 48

# 8 x 7 = 56

# 8 x 8 = 64

# 8 x 9 = 72

# 8 x 10 = 80
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Challenge #8

# Write a Python script that displays the following pattern from 1  to n where n is entered by the user.

# If the user enters 6 it will display:

# 1

# 22

# 333

# 4444

# 55555

# 666666
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(str(i) * i)

# Challenge #9

# Write a Python program that finds the common characters that appear in two given strings.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = []

for char in str1:
    if char in str2 and char not in common:
        common.append(char)

print(f"Common characters: {common}")

# Challenge #10

# Write a Python program that iterates through numbers from 1 to 50 and prints:

# "Foo" for multiples of 3

# "Bar" for multiples of 5

# "FooBar" for multiples of both 3 and 5

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FooBar")
    elif i % 3 == 0:
        print(f"{i}: Foo")
    elif i % 5 == 0:
        print(f"{i}: Bar")
    else:
        print(i)

# Write a Python script that prints out the Fibonacci series up to a given number n.
n = int(input("Enter a number: "))

a = 0
b = 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

# Challenge #12

# Write a Python script that draws the following pattern using for loops.

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * *

# * * *

# * *

# *

n = 5

# Top half (1 to 5)
for i in range(1, n + 1):
    print("* " * i)

# Bottom half (4 to 1)
for i in range(n - 1, 0, -1):
    print("* " * i)
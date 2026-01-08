#

# ===== VARIABLES AND DATA TYPES =====

print("=== Variables and Data Types ===")

# Strings (text)
name = "Disego"
greeting = "Hello, World!"
print(greeting)
print(f"My name is {name}")

# Numbers
age = 25
height = 5.9
print(f"Age: {age}, Height: {height}")

# Boolean (True/False)
is_student = True
is_working = False
print(f"Student: {is_student}")

# ===== BASIC MATH =====

print("\n=== Basic Math Operations ===")

x = 10
y = 3

print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Integer Division: {x} // {y} = {x // y}")
print(f"Remainder: {x} % {y} = {x % y}")
print(f"Power: {x} ** {y} = {x ** y}")

# ===== LISTS =====

print("\n=== Working with Lists ===")

# Create a list
fruits = ["apple", "banana", "orange", "grape"]
print(f"Fruits: {fruits}")

# Access items
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Add items
fruits.append("mango")
print(f"After adding mango: {fruits}")

# Remove items
fruits.remove("banana")
print(f"After removing banana: {fruits}")

# Length of list
print(f"Number of fruits: {len(fruits)}")

# ===== IF STATEMENTS =====

print("\n=== If Statements ===")

temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("Nice weather!")
else:
    print("It's cold!")

# Check if number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# ===== FUNCTIONS =====

print("\n=== Functions ===")

# Simple function
def greet():
    print("Hello from a function!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Disego")
greet_person("Noah")

# Function that returns a value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function to calculate area of rectangle
def rectangle_area(length, width):
    area = length * width
    return area

area = rectangle_area(10, 5)
print(f"Rectangle area: {area}")

# ===== DICTIONARIES =====

print("\n=== Dictionaries ===")

# Create a dictionary
person = {
    "name": "Disego",
    "age": 25,
    "city": "Johannesburg",
    "student": True
}

print(f"Person info: {person}")
print(f"Name: {person['name']}")
print(f"City: {person['city']}")

# Add new key
person["email"] = "disegonoah@gmail.com"
print(f"Updated person: {person}")

# ===== STRING METHODS =====

print("\n=== String Methods ===")

text = "python programming"

print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title case: {text.title()}")
print(f"Replace: {text.replace('python', 'Python')}")
print(f"Split: {text.split()}")

# ===== INPUT (Commented out for auto-run) =====

print("\n=== User Input Example (commented) ===")
print("# Uncomment these lines to try user input:")
print("# user_name = input('What is your name? ')")
print("# print(f'Nice to meet you, {user_name}!')")

# ===== SIMPLE CALCULATOR =====

print("\n=== Simple Calculator ===")

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"

print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")

# ===== CHECK IF PRIME NUMBER =====

print("\n=== Check Prime Number ===")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

test_numbers = [2, 7, 10, 13, 20]
for num in test_numbers:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

print("\n=== Program Complete! ===")
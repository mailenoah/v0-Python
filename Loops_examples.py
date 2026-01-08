

# Example 1: Basic for loop with range
print("=== Example 1: Count from 0 to 4 ===")
for i in range(5):
    print(f"Number: {i}")

# Example 2: For loop with start and end
print("\n=== Example 2: Count from 1 to 5 ===")
for i in range(1, 6):
    print(f"Number: {i}")

# Example 3: For loop with step
print("\n=== Example 3: Even numbers from 0 to 10 ===")
for i in range(0, 11, 2):
    print(f"Even number: {i}")

# Example 4: Loop through a list
print("\n=== Example 4: Loop through fruits ===")
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Example 5: Loop with index using enumerate
print("\n=== Example 5: Loop with index ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# ===== WHILE LOOPS =====

# Example 6: Basic while loop
print("\n=== Example 6: Countdown with while ===")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

# Example 7: While loop with user input simulation
print("\n=== Example 7: Sum numbers until 0 ===")
numbers = [5, 10, 15, 0, 20]  # Simulating user input
total = 0
i = 0
while i < len(numbers) and numbers[i] != 0:
    total += numbers[i]
    print(f"Added {numbers[i]}, total is now {total}")
    i += 1
print(f"Final total: {total}")

# ===== NESTED LOOPS =====

# Example 8: Nested for loops - multiplication table
print("\n=== Example 8: 3x3 Multiplication Table ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  |  ")
    print()  # New line after each row

# Example 9: Pattern printing
print("\n=== Example 9: Star Pattern ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line

# ===== LOOP CONTROL =====

# Example 10: Break statement
print("\n=== Example 10: Break - Find first number > 15 ===")
numbers = [5, 10, 12, 18, 20, 25]
for num in numbers:
    if num > 15:
        print(f"Found {num}! Stopping search.")
        break
    print(f"Checking {num}...")

# Example 11: Continue statement
print("\n=== Example 11: Continue - Skip odd numbers ===")
for i in range(1, 11):
    if i % 2 != 0:  # If odd
        continue  # Skip to next iteration
    print(f"Even number: {i}")

# Example 12: Loop with else
print("\n=== Example 12: Loop with else clause ===")
for i in range(3):
    print(f"Loop iteration {i}")
else:
    print("Loop completed normally!")

# ===== PRACTICAL EXAMPLES =====

# Example 13: Calculate sum and average
print("\n=== Example 13: Sum and Average ===")
scores = [85, 92, 78, 90, 88]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Total: {total}, Average: {average}")

# Example 14: Find maximum value
print("\n=== Example 14: Find Maximum ===")
numbers = [45, 23, 67, 12, 89, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum number: {max_num}")

# Example 15: Reverse a string
print("\n=== Example 15: Reverse a String ===")
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")
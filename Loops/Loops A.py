#Snippet 1 
print("hello")

for i in range(5):
    print("code")

print("goodbye")

#Snippet 2 
print("hi")

for i in range(3, 8):
    print("program")
    print(i)

print("bye")

#Snippet 3
def foo():
    for num in range(10, 0, -2):
        print(num)

print("begin")
foo()
print("end")
foo()

#Snippet 4
word = "street"

for i in range(len(word)):
    print(i)
    print(word[i])

#Snippet 5
total = 0

for i in range(1, 5):
    total += i
    print(total)

print("grand total:", total)

#1️⃣ one_to_four.py
def one_to_four():
    for i in range(1, 5):
        print(i)
one_to_four()

#2️⃣ count_up.py
# Write a function `count_up(max_num)` that prints numbers from 1 to max_num.



def count_up(max_num):
    for i in range(1, max_num + 1):
        print(i)
count_up(5)
count_up(3)

## 3️⃣ **min_to_max.py**

# Write a function `min_to_max(min_num, max_num)` that prints all numbers from min to max inclusive.
def min_to_max(min_num, max_num):
    for i in range(min_num, max_num + 1):
        print(i)
min_to_max(5, 9)
min_to_max(11, 13)
min_to_max(20, 11)   # what happens here?

#4️⃣ string_iterate.py
# Write a function `string_iterate(text)` that prints each character of the string.

def string_iterate(text):
    for char in text:
        print(char)
string_iterate("celery")
print("Wonderful, word completed, lets starts a new one below")
string_iterate("hat")

#5️⃣ evens.py

# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
    for i in range(2, max_num, 2):
        print(i)
evens(11)
evens(8)

## 🔥 **6️⃣ sum_of_range.py**

#Write `sum_of_range(n)`

#Print the sum of numbers from 1 to n
def sum_of_range(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)
sum_of_range(5)
# prints: 15

#🔥 7️⃣ countdown.py
def countdown(start):
    for i in range(start, 0, -1):
        print(i)
countdown(5)
# 5
# 4
# 3
# 2
# 1


## 🔥 **8️⃣ find_char_positions.py**

#Write a function that prints all **indexes** where a character appears in a string.
def find_char_positions(text, char):
    for i in range(len(text)):
        if text[i] == char:
            print(i)
find_char_positions("banana", "a")
# 1
# 3
# 5

## 🔥 **9️⃣ multiplication_table.py**

#Print the multiplication table of a number up to 10.
def multiplication_table(number):
    for i in range(1, 11):
        print(number * i)
multiplication_table(4)
# 4
# 8
# 12
# ...
# 40
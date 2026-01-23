#1️⃣ five_multiples_of.py

# Write a function `five_multiples_of(n)` that prints the first five multiples of n.
# The function does not return a value, just prints.


def five_multiples_of(n):
    for i in range(1, 6):
        print(n * i)
five_multiples_of(7)

# 7
# 14
# 21
# 28
# 35

#2️⃣ sum_up_to.py
# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(max_num):
    total = 0
    for i in range(1, max_num + 1):
        total += i
    return total
print(sum_up_to(4))
print(sum_up_to(5))
print(sum_up_to(2))

#3️⃣ no_ohs.py
# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

# Example:
def no_ohs(text):
    for char in text:
        if char != 'o':
            print(char)
no_ohs("code")
# c
# d
# e

#4️⃣ odd_sum.py
# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

# Example:
def odd_sum(max_num):
    total = 0
    for i in range(1, max_num + 1):
        if i % 2 != 0:
            total += i
    return total
print(odd_sum(10)) #-> 25  # 1 + 3 + 5 + 7 + 9
print(odd_sum(5))  #-> 9   # 1 + 3 + 5

#5️⃣ string_repeater.py
# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

# Example:
def string_repeater(text, n):
    result = ""
    for i in range(n):
        result += text
    return result
string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'

#6️⃣ product_up_to.py
# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)
def product_up_to(max_num):
    result = 1
    for i in range(1, max_num + 1):
        result *= i
    return result
# Example:
print(product_up_to(4) )#-> 24
print(product_up_to(5)) #-> 120
print(product_up_to(7) )#-> 5040

#7️⃣ div_by_either.py
# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num that are divisible by num1 or num2.
# The function does not return a value, just prints.
def div_by_either(num1, num2, max_num):
    for i in range(1, max_num):
        if i % num1 == 0 or i % num2 == 0:
            print(i)
# Example:
div_by_either(4, 3, 16)
# 3
# 4
# 6
# 8
# 9
# 12
# 15

def divisible(num1, num2):
    return num1 % num2 == 0
print(divisible(12, 3))    # True
print(divisible(12, 5))    # False
print(divisible(60, 4))    # True
print(divisible(60, 11))   # False
print(divisible(21, 7))    # True
print(divisible(21, 6))    # FalsePy

#2️⃣ case_changer.py
def case_change(text, make_upper):
    if make_upper == True:
        return text.upper()
    else:
        return text.lower()
print(case_change("Super", True))      # SUPER
print(case_change("Super", False))     # super
print(case_change("tAmBourine", True)) # TAMBOURINE
print(case_change("tAmBourine", False))# tambourine

#3️⃣ in_range.py

def in_range(min_val, max_val, n):
    if n >= min_val and n <= max_val:
        return True
    else:
        return False
print(in_range(5, 13, 8))     # True
print(in_range(5, 13, 29))    # False
print(in_range(100, 125, 100))# True
print(in_range(100, 125, 99)) # False
print(in_range(40, 45, 44))   # True
print(in_range(40, 45, 45))   # True
print(in_range(40, 45, 46))   # False


## 4️⃣ **average_of_four.py**

#Write `average_of_four(a, b, c, d)` that returns the average of four numbers.
def average_of_four(a, b, c, d):
    return (a + b + c + d) / 4

print(average_of_four(10, 4, 12, 3))     # 7.25
print(average_of_four(-20, 50, 4, 21))   # 13.75
print(average_of_four(5, 5, 3, 7))       # 5

## 5️⃣ **number_change.py**

#Write a function:

#- If number is **even**, return **half**
#- If number is **odd**, return **doubl**
def number_change(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 2
    
print(number_change(6))   # 3
print(number_change(7))   # 14
print(number_change(16))  # 8
print(number_change(21))  # 42

## 6️⃣ **larger.py**

#Write a function `larger(a, b)`

#Return the **larger** of the two numbers.
def larger(a, b):
    if a > b:
        return a
    else:
        return b
print(larger(256, 400))   # 400
print(larger(31, 4))      # 31
print(larger(-6, 7))      # 7
print(larger(11.3, 11.2)) # 11.3
print(larger(-10, -3))    # -3


## 7️⃣ **contains.py**

#Write a function `contains(str1, str2)` that:

#- Returns **True** if `str2` is found inside `str1`
#- Ignore capitalization differences
def contains(str1, str2):
    if str2.lower() in str1.lower():
        return True
    else:
        return False
print(contains("caterpillar", "pill"))     # True
print(contains("lion's share", "on"))      # True
print(contains("SORRY", "or"))             # True
print(contains("tangent", "gem"))          # False
print(contains("clock", "ok"))             # False


## 🔥 **8️⃣ reverse_string.py**

#Write a function `reverse_string(text)` that returns the reversed string
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))   # olleh
print(reverse_string("Python"))  # nohtyP

## 🔥 **9️⃣ count_vowels.py**

#Write `count_vowels(text)`

#Return how many vowels are in the string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3

## 🔥 **🔟 is_palindrome.py**

#Write a function that checks if a string is a **palindrome** (same forward & backward).

#Ignore spaces and capitalization.

# 🔥 **🔟 is_palindrome.py**

#Write a function that checks if a string is a **palindrome** (same forward & backward).

#Ignore spaces and capitalization.
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    # Reverse the cleaned string
    reversed_text = cleaned[::-1]
    # Check if they're the same
    if cleaned == reversed_text:
        return True
    else:
        return False
print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False



## 🔥 **1️⃣1️⃣ sum_upto.py**

##Write `sum_upto(n)`

#Return the sum of numbers from 1 → n.
def sum_upto(n):
    return sum(range(1, n + 1))
print(sum_upto(5))   # 15
print(sum_upto(10))  # 55


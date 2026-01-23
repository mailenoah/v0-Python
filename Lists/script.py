# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

# Example:
def total(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total([3, 2, 8]) )#-> 13
print(total([-5, 7, 4, 6])) #-> 12
print(total([7])) #-> 7
print(total([])) #-> 0


# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

# Example:
def stay_positive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result
print(stay_positive([10, -4, 3, 6]))#-> [10, 3, 6]
print(stay_positive([-5, 11, -40, 30.3, -2])) #-> [11, 30.3]
print(stay_positive([-11, -30])) #-> []


def bleep_vowels(text):
    result = ""
    vowels = "aeiou"
    for char in text:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

# Examples:
print(bleep_vowels("skateboard"))     # 'sk*t*b**rd'
print(bleep_vowels("slipper"))        # 'sl*pp*r'
print(bleep_vowels("range"))          # 'r*ng*'
print(bleep_vowels("brisk morning"))  # 'br*sk m*rn*ng'


def filter_long_words(words):
    result = []
    for word in words:
        if len(word) < 5:
            result.append(word)
    return result

# Examples:
print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))  # ['kale', 'cat', 'axe']
print(filter_long_words(["disrupt", "pour", "trade", "pic"]))          # ['pour', 'pic']


def num_odds(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

# Examples:
print(num_odds([4, 7, 2, 5, 9]))           # 3
print(num_odds([11, 31, 58, 99, 21, 60]))  # 4
print(num_odds([100, 40, 4]))              # 0

def strings_to_lengths(strings):
    result = []
    for string in strings:
        result.append(len(string))
    return result

# Examples:
print(strings_to_lengths(["belly", "echo", "irony", "pickled"]))  # [5, 4, 5, 7]
print(strings_to_lengths(["on", "off", "handmade"]))              # [2, 3, 8]


# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.
def divisors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

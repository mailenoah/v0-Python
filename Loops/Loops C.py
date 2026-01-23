
def divisible_range(min_val, max_val, num):
 for i in range(min_val, max_val):
  if i % num == 0:
   print(i)
print("First blok")
divisible_range(17, 40, 9)
print("Second blok")
divisible_range(10, 24, 4)


def reverse_iterate(text):
    for i in range(len(text) - 1, -1, -1):
        print(text[i])

# Examples:
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b


# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text):
    result = ""
    for char in text:
        if not char.isupper():
            result += char
    return result

# Examples:
print(remove_capitals("fOrEver"))     # 'frver'
print(remove_capitals("raiNCoat"))    # 'raioat'
print(remove_capitals("cElLAr Door")) # 'clr oor'

def raise_power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

# Examples:
print(raise_power(2, 5))   # 32
print(raise_power(4, 3))   # 64
print(raise_power(10, 4))  # 10000
print(raise_power(7, 2))   # 49


def censor_e(text):
    result = ""
    for char in text:
        if char == "e":
            result += "*"
        else:
            result += char
    return result

# Examples:
print(censor_e("speedy"))   # 'sp**dy'
print(censor_e("pending"))  # 'p*nding'
print(censor_e("scene"))    # 'sc*n*'
print(censor_e("heat"))     # 'h*at'

# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
            print(i)
fizz_buzz(18)
fizz_buzz(33)

#snippet_0_1
def greet():
    print("hey")
    print("programmers")

def whistle():
    print("doot")

print("first")
print("second")
greet()
print("third")
print("fourth")
whistle()

#snippet_0_2
def how_many():
    return 42

print(how_many)
print(how_many())

the_answer = how_many()
print(the_answer)

def how_much():
    5   # does nothing

print(how_much())


#snippet_0_3
def average(num1, num2):
    print("calculating...")
    return (num1 + num2) / 2

print(average(5, 10))
print(average(20, 26))
print(average(50, 100) + 2)

a = 21 + 3
b = 20
n = average(a, b)
print(average(n, 18))


#snippet_0_4
def exclaim(s):
    capitalized = s.upper()
    return capitalized + "!!"

result = exclaim("potato")
print(result)
print(len(result))
print(result[0])
print(result[-1])

#is_div_by_4
# Write a function `is_div_by_4` that accepts a number as an argument.
# The function should return a boolean indicating whether or not
# the number is divisible by 4.
def is_div_by_4(num):
    return num % 4 == 0
print(is_div_by_4(8))   # True
print(is_div_by_4(12))  # True
print(is_div_by_4(24))  # True
print(is_div_by_4(9))   # False
print(is_div_by_4(10))  # False


#keep_it_quiet
# Write a function `keep_it_quiet` that accepts a string as an argument.
# The function should return the lowercase version of the string
# with 3 periods added to the end.
def keep_it_quiet(s):
    return s.lower() + "..."
print(keep_it_quiet("HOORAY"))     # "hooray..."
print(keep_it_quiet("Doggo"))      # "doggo..."
print(keep_it_quiet("WHAT?!?!"))   # "what?!?!..."

#is_long
# Write a function `is_long` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# is longer than 5 characters.
def is_long(s):
    return len(s) > 5
print(is_long("pie"))         # False
print(is_long("kite"))        # False
print(is_long("kitty"))       # False
print(is_long("telescope"))   # True
print(is_long("thermometer")) # True
print(is_long("restaurant"))  # True

#half
# Write a function `half` that accepts a number as an argument.
# The function should return half of the number.
def half(num):
    return num / 2
print(half(8))    # 4
print(half(15))   # 7.5
print(half(90))   # 45


#ends_with_t
# Write a function `ends_with_t` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# ends with the character "t".
def ends_with_t(s):
    return s[-1] == "t"
print(ends_with_t("smart"))      # True
print(ends_with_t("racket"))     # True
print(ends_with_t("taco"))       # False
print(ends_with_t("boomerang"))  # False


#average
# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

# Example:
# make_acronym("New York") -> 'NY'
# make_acronym("same stuff different day") -> 'SSDD'
# make_acronym("Laugh out loud") -> 'LOL'
# make_acronym("don't over think stuff") -> 'DOTS'

def make_acronym(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Get the first character of each word and convert to uppercase
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    
    return acronym


# Test the function
print(make_acronym("New York"))  # Output: NY
print(make_acronym("same stuff different day"))  # Output: SSDD
print(make_acronym("Laugh out loud"))  # Output: LOL
print(make_acronym("don't over think stuff"))  # Output: DOTS

def reverse_array(arr):
    return arr[::-1]


# Test the function
print(reverse_array(["zero", "one", "two", "three"]))  # Output: ['three', 'two', 'one', 'zero']
print(reverse_array([7, 1, 8]))  # Output: [8, 1, 7]

def your_average_function(numbers):
    if len(numbers) == 0:
        return None
    
    total = sum(numbers)
    average = total / len(numbers)
    return average


# Test the function
print(your_average_function([5, 2, 7, 24]))  # Output: 9.5
print(your_average_function([100, 6]))  # Output: 53.0
print(your_average_function([31, 32, 40, 12, 33]))  # Output: 29.6
print(your_average_function([]))  # Output: None

def choose_divisibles(numbers, target):
    divisibles = []
    for num in numbers:
        if num % target == 0:
            divisibles.append(num)
    return divisibles


# Test the function
print(choose_divisibles([40, 7, 22, 20, 24], 4))  # Output: [40, 20, 24]
print(choose_divisibles([9, 33, 8, 17], 3))  # Output: [9, 33]
print(choose_divisibles([4, 25, 1000], 10))  # Output: [1000]

def maximum(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)


# Test the function
print(maximum([5, 6, 3, 7]))  # Output: 7
print(maximum([17, 15, 19, 11, 2]))  # Output: 19
print(maximum([]))  # Output: None

def word_count(sentence, target_words):
    words = sentence.split()
    count = 0
    for word in words:
        if word in target_words:
            count += 1
    return count


# Test the function
print(word_count("open the window please", ["please", "open", "sorry"]))  # Output: 2
print(word_count("drive to the cinema", ["the", "driver"]))  # Output: 1
print(word_count("can I have that can", ["can", "I"]))  # Output: 3
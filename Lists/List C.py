def lengthiest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) >= len(longest):
            longest = word
    return longest

# Examples:
print(lengthiest_word("I am pretty hungry"))                # 'hungry'
print(lengthiest_word("we should think outside of the box")) # 'outside'
print(lengthiest_word("down the rabbit hole"))               # 'rabbit'
print(lengthiest_word("simmer down"))                        # 'simmer'

def alternating_caps(sentence):
    words = sentence.split()
    result = []
    for i in range(len(words)):
        if i % 2 == 0:
            result.append(words[i].lower())
        else:
            result.append(words[i].upper())
    return " ".join(result)

# Examples:
print(alternating_caps("take them to school"))        # 'take THEM to SCHOOL'
print(alternating_caps("What did ThEy EAT before?"))  # 'what DID they EAT before?'

def number_range(min_val, max_val, step):
    result = []
    current = min_val
    while current <= max_val:
        result.append(current)
        current += step
    return result

# Examples:
print(number_range(10, 40, 5))  # [10, 15, 20, 25, 30, 35, 40]
print(number_range(14, 24, 3))  # [14, 17, 20, 23]
print(number_range(8, 35, 6))   # [8, 14, 20, 26, 32]

def remove_short_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return " ".join(result)

# Examples:
print(remove_short_words("knock on the door will you"))  # 'knock door will'
print(remove_short_words("a terrible plan"))             # 'terrible plan'
print(remove_short_words("run faster that way"))         # 'faster that'

               # [4, 7]
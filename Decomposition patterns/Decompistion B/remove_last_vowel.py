# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(string):
    vowels = "aeiouAEIOU"
    last_vowel_index = -1
    
    for i in range(len(string)):
        if string[i] in vowels:
            last_vowel_index = i
    
    if last_vowel_index == -1:
        return string
    
    result = ""
    for i in range(len(string)):
        if i != last_vowel_index:
            result += string[i]
    
    return result

print(remove_last_vowel("speaker"))  # 'speakr'
print(remove_last_vowel("trading"))  # 'tradng'
print(remove_last_vowel("thunder"))  # 'thundr'
print(remove_last_vowel("myth"))     # 'myth'
# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

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

def trendy_text(sentence):
    words = sentence.split()
    result = ""
    
    for word in words:
        new_word = remove_last_vowel(word)
        result += new_word
        result += " "
    
    return result.strip()

print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'
print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'
print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'
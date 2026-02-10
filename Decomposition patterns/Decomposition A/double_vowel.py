def double_vowel(string):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in string:
        result += char
        if char in vowels:
            result += char
    
    return result

# Example usage:
print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'
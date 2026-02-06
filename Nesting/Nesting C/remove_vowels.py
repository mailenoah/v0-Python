def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
                break
        if not is_vowel:
            result += char
    return result

# Example usage:
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'
def remove_first_vowel(s):
    vowels = "aeiouAEIOU"
    result = ""
    found_first_vowel = False
    for char in s:
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
                break
        if is_vowel and not found_first_vowel:
            found_first_vowel = True
        else:
            result += char
    return result

# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'
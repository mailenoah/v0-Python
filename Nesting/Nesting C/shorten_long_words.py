def shorten_long_words(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    result = ""
    
    for word in words:
        if len(word) > 4:
            new_word = ""
            for char in word:
                is_vowel = False
                for vowel in vowels:
                    if char == vowel:
                        is_vowel = True
                        break
                if not is_vowel:
                    new_word += char
            result += new_word
        else:
            result += word
        result += " "
    
    return result.strip()

# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
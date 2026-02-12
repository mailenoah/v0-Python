def lala_language(sentence):
    words = sentence.split(" ")
    result = []

    for word in words:
        if len(word) > 3:
            new_word = change_vowel(word)
            result.append(new_word)
        else:
            result.append(word)

    return " ".join(result)


def change_vowel(word):
    vowels = "aeiou"
    changed_word = ""

    for char in word:
        if char in vowels:
            changed_word += char + "l" + char
        else:
            changed_word += char

    return changed_word


print(lala_language('this is pretty strange'))
print(lala_language('can you speak our language'))
def funny_phrase(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    result = ""
    
    for i in range(len(words)):
        word = words[i]
        if i % 2 == 1:
            new_word = ""
            for char in word:
                new_word += char
                if char in vowels:
                    new_word += char
            result += new_word
        else:
            result += word
        result += " "
    
    return result.strip()

# Example usage:
print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'
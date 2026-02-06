def word_replace(sentence, replacements):
    words = sentence.split()
    result = ""
    
    for word in words:
        if word in replacements:
            result += replacements[word]
        else:
            result += word
        result += " "
    
    return result.strip()

# Example usage:
print(word_replace(
    "I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
    "the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
    "I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'
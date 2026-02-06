def letter_map(string, mapping):
    result = ""
    
    for char in string:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    
    return result

# Example usage:
print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'
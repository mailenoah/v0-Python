def character_count(string):
    result = {}
    
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    
    return result

# Example usage:
print(character_count("evening"))
# { 'e': 2, 'v': 1, 'n': 2, 'i': 1, 'g': 1 }

print(character_count("mississippi"))
# { 'm': 1, 'i': 4, 's': 4, 'p': 2 }

print(character_count("chili"))
# { 'c': 1, 'h': 1, 'i': 2, 'l': 1 }
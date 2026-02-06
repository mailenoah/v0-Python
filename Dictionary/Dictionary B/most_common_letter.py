def most_common_letter(string):
    counts = {}
    
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    max_char = None
    max_count = 0
    
    for char in counts:
        if counts[char] > max_count:
            max_count = counts[char]
            max_char = char
    
    return max_char

# Example usage:
print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'
# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.

def pick_prefix(strings, prefix):
    result = []
    prefix_length = len(prefix)
    
    for word in strings:
        if len(word) >= prefix_length:
            matches = True
            for i in range(prefix_length):
                if word[i] != prefix[i]:
                    matches = False
                    break
            if matches:
                result.append(word)
    
    return result

print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']
print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']
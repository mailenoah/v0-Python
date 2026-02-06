def spam(pairs):
    result = ""
    for pair in pairs:
        word = pair[0]
        count = pair[1]
        for i in range(count):
            result += word
            if i < count - 1 or pair != pairs[-1]:
                result += " "
    return result.strip()

# Example usage:
array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  # 'hi hi hi bye bye'
array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))  # 'cat dog dog bird bird bird bird'
def max_object_value(dictionary):
    max_key = None
    max_value = None
    
    for key in dictionary:
        value = dictionary[key]
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    
    return [max_key, max_value]

# Example usage:
print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
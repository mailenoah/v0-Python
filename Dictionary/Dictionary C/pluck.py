def pluck(dictionary, keys):
    result = {}
    
    for key in keys:
        if key in dictionary:
            result[key] = dictionary[key]
    
    return result

# Example usage:
print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }
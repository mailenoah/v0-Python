def object_add(dict1, dict2):
    result = {}
    
    for key in dict1:
        result[key] = dict1[key]
    
    for key in dict2:
        if key in result:
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]
    
    return result

# Example usage:
obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }

obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }


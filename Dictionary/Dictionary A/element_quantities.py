def element_quantities(quantities):
    result = []
    for element in quantities:
        count = quantities[element]
        for i in range(count):
            result.append(element)
    return result

# Example usage:
quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']
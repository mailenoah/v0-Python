def secret_cipher(string, cipher):
    result = ""
    
    for char in string:
        if char in cipher:
            result += cipher[char]
        else:
            result += "?"
    
    return result

# Example usage:
print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'
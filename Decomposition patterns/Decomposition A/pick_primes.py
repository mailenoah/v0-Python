def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def pick_primes(numbers):
    result = []
    
    for num in numbers:
        if is_prime(num):
            result.append(num)
    
    return result

# Example usage:
print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []
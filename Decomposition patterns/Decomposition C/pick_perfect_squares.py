def pick_perfect_squares(numbers):
    result = []

    for num in numbers:
        for i in range(1, num):
            if i * i == num:
                result.append(num)

    return result


print(pick_perfect_squares([6, 4, 81, 21, 36]))
print(pick_perfect_squares([100, 24, 144]))
print(pick_perfect_squares([30, 25]))

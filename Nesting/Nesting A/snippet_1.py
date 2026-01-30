# Predict what this will print:

# Predict what this will print:
for i in range(1, 5):
    for j in range(1, 4):
        print(i, j)

for n in range(2):
    print("n=" + str(n))
    for m in range(5):
        print("   m=" + str(m))
    print("n=" + str(n))

friends = ["philip", "abby", "phelipe", "simcha"]

for i in range(len(friends)):
    for j in range(len(friends)):
        print(friends[i], friends[j])

locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        print(locations[i], locations[j])

colors = ["red", "purple", "orange"]

for color_str in colors:
    print(color_str)
    for char in color_str:
        print(char)


def pair_print(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i] + " - " + arr[j])

# Example:
pair_print(["artichoke", "broccoli", "carrot", "daikon"])
# artichoke - broccoli
# artichoke - carrot
# artichoke - daikon
# broccoli - carrot
# broccoli - daikon
# carrot - daikon


def print_combinations(arr1, arr2):
    for elem1 in arr1:
        for elem2 in arr2:
            print(elem1 + " " + elem2)

# Example:
colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors, clothes)
# gray shirt
# gray flannel
# cream shirt
# cream flannel
# cyan shirt
# cyan flannel

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False

# Examples:
print(two_sum([2, 3, 5, 9], 7))   # True
print(two_sum([2, 3, 5, 9], 4))   # False
print(two_sum([6, 3, 4], 10))     # True
print(two_sum([6, 5, 1], 10))     # False
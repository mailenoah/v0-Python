restaurant = {
"name":"Bob's Burgers",
"location":"123 Ocean Avenue",
"owners": ["Bob Belcher","Linda Belcher"],
"established":2011,
"menu": ["burgers","fries","shakes"],
}

print("owners"in restaurant)
print("employees"in restaurant)

some_key ="menu"
print(some_key in restaurant)

print(restaurant["menu"])
print(restaurant.get("menu"))
print(restaurant[some_key])
print(restaurant.get("some_key"))

print("fries"in restaurant["menu"])


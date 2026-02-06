recipe = {
"name":"Old Fashioned Pancakes",
"difficulty":"easy",
"tasty":True,
"ingredients": ["eggs","milk","butter","flour","sugar"],
}

print(recipe["name"])
print(recipe["name"])
print(len(recipe["ingredients"]))
print(recipe.get("calories"))

some_variable ="difficulty"
print(recipe[some_variable])
print(recipe.get("some_variable"))

for ingredient in recipe ["ingredients"]:
 print (ingredient)


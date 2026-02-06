movie = {
"title":"Fight Club",
"year":1999,
"genre": ["drama","thriller"],
"starring": ["Brad Pitt","Edward Norton"],
}

print(movie["year"])
print(movie["title"])
print(movie["genre"])
print(movie["genre"][0])
print(movie["genre"][1])

print(movie.get("duration"))
print(movie["starring"][1])
print(len(movie["starring"]))


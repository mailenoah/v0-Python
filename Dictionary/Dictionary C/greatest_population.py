def greatest_population(countries):
    max_country = None
    max_population = 0
    
    for country in countries:
        if country["population"] > max_population:
            max_population = country["population"]
            max_country = country["name"]
    
    return max_country

# Example usage:
countries1 = [
    {"name":"Cameroon","population":27744989,"gdp":38.68 },
    {"name":"Belarus","population":9477918,"gdp":59.66 },
    {"name":"Indonesia","population":267026366,"gdp":1042 },
    {"name":"Guyana","population":750204,"gdp":3.88 },
]
print(greatest_population(countries1))
# 'Indonesia'

countries2 = [
    {"name":"New Zealand","population":4925477,"gdp":204.9 },
    {"name":"Mozambique","population":30098197,"gdp":14.72 },
    {"name":"Greenland","population":57616,"gdp":2.71 },
    {"name":"Kazakhstan","population":19091949,"gdp":179.3 },
    {"name":"Burma","population":56590071,"gdp":71.21 },
]
print(greatest_population(countries2))
# 'Burma'
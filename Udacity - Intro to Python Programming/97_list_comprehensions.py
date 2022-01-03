cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

print("Criando lista com append(): ", capitalized_cities)

capitalized_cities = [city.title() for city in cities]
print("list comprehension: ", capitalized_cities)
cities = ["berlin", "tokyo", "tokyo", "berlin", "lima", "brooklyn", "berlin"]

# DUPLICATE REMOVER
for city in cities:
    if cities.count(city) > 1:
        cities.remove(city)

print(cities)
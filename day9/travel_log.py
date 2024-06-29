travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(country_name, total_visits, list_of_cities):
    travel_log.append({
        "country": country_name,
        "visits": total_visits,
        "cities": list_of_cities
    })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
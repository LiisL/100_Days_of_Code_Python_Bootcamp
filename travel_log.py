travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_visited, times_visited, cities_list):
   new_countery = {}
   new_countery["country"] = country_visited
   new_countery["visits"] = times_visited
   new_countery["cities"] = cities_list
   travel_log.append(new_countery)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
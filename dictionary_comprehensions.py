# dictionary = {key : expression for (key,value) in iterable}

cities_in_f = {"New York":100,"Los Angeles":75,"Chicago":68,"Tokyo":50}
cities_in_c = {key:round((value-32)*(5/9)) for key,value in cities_in_f.items()}
print(cities_in_c)

print("----------------------------------")

weather = {"New York":"Snowing","Los Angeles":"Cloudy","Chicago":"Rainy","Tokyo":"Sunny"}
sunny_weather = {key : value for key,value in weather.items() if value == "Sunny"}
print(sunny_weather)

print("----------------------------------")

desc_cities = {key : ("warm" if value >= 35 else "cold") for key,value in cities_in_c.items()}
print(desc_cities)

print("----------------------------------")

def check_temp(value):
    if value >= 35:
        return "hot"
    else:
        return "cool"

cities_desc = {key: check_temp(value) for key,value in cities_in_c.items()}
print(cities_desc)

print("----------------------------------")
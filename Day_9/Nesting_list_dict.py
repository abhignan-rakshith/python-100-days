# Nesting
capitals = {
    "Paris": "France",
    "Tokyo": "Japan",
    "Rome": "Italy",
    "Moscow": "Russia",
    "Berlin": "Germany"
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lyon", "Nantes"],
    "Germany": ["Berlin", "Munich", "Hamburg"]
}

# Nesting a dictionary in dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon", "Nantes"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Hamburg"], "total_visits": 8},
    "Japan": {"cities_visited": ["Tokyo", "Osaka", "Kyoto"], "total_visits": 21},
    "Russia": {"cities_visited": ["Moscow", "Samara", "St. Petersburg"], "total_visits": 4},
    "Italy": {"cities_visited": ["Rome", "Venice", "Naples"], "total_visits": 18},
}

# Nesting a dictionary in a list

travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lyon", "Nantes"], 
        "total_visits": 12
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Hamburg"], 
        "total_visits": 8
    },
    {
        "Country": "Japan",
        "cities_visited": ["Tokyo", "Osaka", "Kyoto"], 
        "total_visits": 21
    },
    {
        "Country": "Russia",
        "cities_visited": ["Moscow", "Samara", "St. Petersburg"], 
        "total_visits": 4
    },
    {
        "Country": "Italy",
        "cities_visited": ["Rome", "Venice", "Naples"], 
        "total_visits": 18
    },
]

# print(travel_log[2])
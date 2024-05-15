import pandas as pd
import random

# Dummy data for farm names and scopes
farm_names = ["Farm" + str(i) for i in range(1, 101)]
scopes = [
    "Vegetal Products",
    "Animal Products",
    "Mushrooms",
    "Food Processing",
    "Vegetal Products, Food Processing",
    "Vegetal Products, Animal Products",
    "Vegetal Products, Mushrooms",
]

# Dictionary for state abbreviations and full names
state_mapping = {
    "Acre": "AC",
    "Alagoas": "AL",
    "Amazonas": "AM",
    "Amapá": "AP",
    "Bahia": "BA",
    "Ceará": "CE",
    "Distrito Federal": "DF",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Minas Gerais": "MG",
    "Mato Grosso do Sul": "MS",
    "Mato Grosso": "MT",
    "Pará": "PA",
    "Paraíba": "PB",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Paraná": "PR",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Rio Grande do Sul": "RS",
    "Santa Catarina": "SC",
    "Sergipe": "SE",
    "São Paulo": "SP",
    "Tocantins": "TO",
}

# Create a list of state abbreviations
state_abbreviations = list(state_mapping.values())

# Dummy data for products // count unique products
products = [
    "banana",
    "apple",
    "lettuce",
    "tomato",
    "potato",
    "carrot",
    "onion",
    "mushroom",
    "chicken",
    "beef",
]

countries = ["Brasil", "Argentina", "Colombia", "Noruega"]

# Create a dictionary to hold the data
data = {
    "name": random.choices(farm_names, k=100),
    "state": random.choices(state_abbreviations, k=100),
    "country": random.choices(countries, k=100),
    "scope": random.choices(scopes, k=100),
}

# Add columns for each product with random 0s and 1s
for product in products:
    data[product] = [random.randint(0, 1) for _ in range(100)]


# load dataframe


# Create DataFrame
df = pd.DataFrame(data)

# df = pd.read_csv('dummies_df.csv')

df["scope"] = df["scope"].str.split(", ")

# Display the first few rows of the DataFrame
# df.head()

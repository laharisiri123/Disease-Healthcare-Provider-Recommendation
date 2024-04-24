import pandas as pd
import numpy as np
import random

# Read the providers data from the CSV file
providers_df = pd.read_csv('datasets/providers.csv')

# Generate user ratings data
user_ratings = []
for _, provider in providers_df.iterrows():
    name = provider['name']
    num_ratings = random.randint(20, 50)
    ratings = [random.randint(1, 5) for _ in range(num_ratings)]
    user_ratings.extend([{'name': name, 'rating': rating} for rating in ratings])

# Create a DataFrame from the list of user ratings
user_ratings_df = pd.DataFrame(user_ratings)

# Save the DataFrame to a CSV file
user_ratings_df.to_csv('datasets/user_ratings.csv', index=False)
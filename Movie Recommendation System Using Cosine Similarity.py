import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

# Step 1: Load the synthetic dataset
try:
    ratings = pd.read_csv('D:\Synthetic_Rating_Movie.csv')
except Exception as e:
    print(f"An error occurred while loading the synthetic dataset: {e}")
    exit()

# Ensure the ratings data is properly loaded
if ratings.empty:
    print("The ratings dataset is empty. Exiting.")
    exit()

# Step 2: Data Preprocessing
# Create the ratings matrix
try:
    ratings_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating')
    ratings_matrix.fillna(0, inplace=True)
except Exception as e:
    print(f"An error occurred during pivot table creation: {e}")
    ratings_matrix = pd.DataFrame()  # Create an empty DataFrame for safe error handling

# Ensure the ratings matrix is properly created
if ratings_matrix.empty:
    print("The ratings matrix is empty. Exiting.")
    exit()

# Step 3: Build the Recommendation Model
# Calculate cosine similarity between users
try:
    user_similarity = cosine_similarity(ratings_matrix)
    user_similarity = pd.DataFrame(user_similarity, index=ratings_matrix.index, columns=ratings_matrix.index)
except Exception as e:
    print(f"An error occurred during similarity calculation: {e}")
    user_similarity = pd.DataFrame()  # Create an empty DataFrame for safe error handling

# Ensure user similarity matrix is properly created
if user_similarity.empty:
    print("The user similarity matrix is empty. Exiting.")
    exit()

# Function to recommend movies based on user similarity
def recommend_movies(user_id, num_recommendations=5):
    try:
        similar_users = user_similarity.loc[user_id].sort_values(ascending=False).index[1:]
        user_ratings = ratings_matrix.loc[user_id]
        recommendations = pd.Series(dtype='float64')  # Explicitly set dtype to float64
        
        for similar_user in similar_users:
            similar_user_ratings = ratings_matrix.loc[similar_user]
            for movie_id in similar_user_ratings.index:
                if user_ratings[movie_id] == 0 and similar_user_ratings[movie_id] > 0:
                    if movie_id not in recommendations:
                        recommendations[movie_id] = 0.0
                    recommendations[movie_id] += similar_user_ratings[movie_id] * user_similarity.at[user_id, similar_user]
        
        recommendations = recommendations.sort_values(ascending=False)
        return recommendations.head(num_recommendations)
    except Exception as e:
        print(f"An error occurred during recommendation generation: {e}")
        return pd.Series(dtype='float64')

# Step 4: Evaluate the Model
# Calculate Mean Squared Error (MSE) to evaluate the model performance
def calculate_mse():
    try:
        predicted_ratings = ratings_matrix.copy()
        for user in ratings_matrix.index:
            recommendations = recommend_movies(user, len(ratings_matrix.columns))
            for movie_id in recommendations.index:
                predicted_ratings.at[user, movie_id] = recommendations[movie_id]

        mse = mean_squared_error(ratings_matrix.values, predicted_ratings.values)
        return mse
    except Exception as e:
        print(f"An error occurred during MSE calculation: {e}")
        return None

# Example to recommend movies for a user
user_id = 1
print(f"Top recommendations for User {user_id}:")
print(recommend_movies(user_id))

# Evaluate the model
mse = calculate_mse()
print(f"Mean Squared Error of the recommendation system: {mse}")

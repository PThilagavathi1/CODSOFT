from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Dataset
data = {
    'Movie_ID': [1, 2, 3, 4, 5],
    'Title': ['Inception', 'Interstellar', 'Dunkirk', 'The Prestige', 'Memento'],
    'Description': [
        'A thief who steals corporate secrets through dream-sharing technology.',
        'Explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.',
        'Allied soldiers are surrounded by the German army during World War II.',
        'Two magicians engage in a battle to create the ultimate illusion.',
        'A man with short-term memory loss attempts to track down his wife’s murderer.'
    ]
}

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(data)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Description'])

# Function to recommend movies
def recommend_movies_tfidf(movie_title, num_recommendations=3):
    # Find the movie in the dataset
    try:
        movie_index = df[df['Title'].str.lower() == movie_title.lower()].index[0]
    except IndexError:
        return f"Movie '{movie_title}' not found in the dataset."
    
    # Calculate cosine similarity with all other movies
    cosine_sim = cosine_similarity(tfidf_matrix[movie_index], tfidf_matrix).flatten()
    
    # Get indices of movies sorted by similarity
    similar_indices = cosine_sim.argsort()[::-1]
    
    # Exclude the movie itself and select top recommendations
    similar_indices = [i for i in similar_indices if i != movie_index][:num_recommendations]
    
    # Get recommended movie titles
    recommendations = df.iloc[similar_indices]['Title'].tolist()
    return recommendations

# Example usage
movie_to_search = 'Inception'
recommendations_tfidf = recommend_movies_tfidf(movie_to_search)
print(f"Movies similar to '{movie_to_search}' using TF-IDF: {recommendations_tfidf}")
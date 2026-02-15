import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize


class MovieRecommender:

    def __init__(self, movies_df):
        """
        movies_df must contain:
        - 'title' column
        - 'tags' column
        """

        self.movies = movies_df.reset_index(drop=True)

        # Initialize vectorizer
        self.vectorizer = CountVectorizer(
            max_features=5000,
            stop_words="english",
            ngram_range=(1, 2)
        )

        # Convert text to vectors (sparse matrix)
        self.vectors = self.vectorizer.fit_transform(self.movies["tags"])

        # Normalize vectors for cosine similarity
        self.vectors = normalize(self.vectors)

    def recommend(self, movie_title, top_n=6):
        """
        Returns top_n similar movies based on title
        """

        # Find index of the selected movie
        matches = self.movies[self.movies["title"] == movie_title]

        if matches.empty:
            return "Movie not found"

        movie_index = matches.index[0]

        # Compute cosine similarity using dot product
        similarity_scores = self.vectors[movie_index].dot(self.vectors.T)
        similarity_scores = similarity_scores.toarray().flatten()

        # Get top similar movie indices (excluding itself)
        sorted_indices = np.argsort(similarity_scores)[::-1]
        top_indices = sorted_indices[1:top_n + 1]

        # Return only movie titles
        return self.movies.iloc[top_indices][["title"]]

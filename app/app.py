from numpy import test
import streamlit as st
import pickle
import pandas as pd
import streamlit as st
from movie_recommender.models.model import MovieRecommender
from movie_recommender.utils.poster import fetch_poster
import sys
import os

sys.path.append(os.path.abspath("src"))


movies_df = pd.read_csv(r"C:\Users\mbvin\OneDrive\Desktop\Movie-Recommendation-System\data\preprocessed\final_data.csv")


st.title("Movie Recommender")



mv = MovieRecommender(movies_df)
movie = st.selectbox("Tell me your favorite movie", movies_df['title'].values)

recommended = mv.recommend(movie)

# if st.button('Recommend'):
#     for i in recommended.iterrows():
#         poster_url = fetch_poster(i[0])
#         st.image(poster_url)
#         st.write(i["title"])

# if st.button('Recommend'):
#     st.write(recommended)

# @st.cache_data
# def cached_fetch(movie_id):
#     return fetch_poster(movie_id)

if st.button("Recommend"):

    recommended = mv.recommend(movie)
    cols = st.columns(3)

    for idx, (_, row) in enumerate(recommended.iterrows()):

        poster_url = fetch_poster(row["movie_id"])

        with cols[idx % 3]:
            if poster_url:
                st.image(poster_url, width = 75)
            else:
                st.write("Poster not available")

            st.write(row["title"])


if __name__ == "__main__":
    st.write("")

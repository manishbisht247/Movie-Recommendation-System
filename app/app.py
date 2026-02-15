from numpy import test
import streamlit as st
import pickle
import pandas as pd
import streamlit as st
from movie_recommender.models.model import MovieRecommender

movies_df = pd.read_csv(r"C:\Users\mbvin\OneDrive\Desktop\Movie-Recommendation-System\data\preprocessed\final_data.csv")


st.title("Movie Recommender")



mv = MovieRecommender(movies_df)
movie = st.selectbox("Tell me your favorite movie", movies_df['title'].values)

recommended = mv.recommend(movie)


if st.button('Recommend'):
    st.write(recommended)


if __name__ == "__main__":
    st.write("")

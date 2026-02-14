import streamlit as st
import pickle
import pandas as pd
import streamlit as st

st.title("Movie Recommender")

def load_data():
    with open('src/movie_recommender/models/movies.pkl', 'rb') as file:
        movies = pickle.load(file)
    return movies
def load_model():
    with open('src/movie_recommender/models/similarity.pkl', 'rb') as file:
        similarity = pickle.load(file)
    return similarity

def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    rank = sorted(list(enumerate(similarity[movie_idx])), reverse = True, key = lambda x: x[1])[1:6]
    frames = []
    for i in rank:
        movies_id = i[0]
        # fetch poster code



        frames.append(movies['title'].iloc[i[0]])
    return frames

movies = load_data()
similarity = load_model()
movie = st.selectbox("Tell me your favorite movie", movies['title'].values)

recommended = recommend(movie)


if st.button('Recommend'):
    st.write(recommended)


if __name__ == "__main__":
    st.write("")

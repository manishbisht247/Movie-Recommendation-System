# import sys
# from pathlib import Path

# ROOT = Path(__file__).resolve().parent
# sys.path.append(str(ROOT / "src"))
# from numpy import test
# import streamlit as st
# import pandas as pd
# from movie_recommender.models.model import MovieRecommender
# from movie_recommender.utils.poster import fetch_poster


# movies_df = pd.read_csv(r"C:\Users\mbvin\OneDrive\Desktop\Movie-Recommendation-System\data\preprocessed\final_data.csv")


# st.title("Movie Recommender")



# mv = MovieRecommender(movies_df)
# movie = st.selectbox("Tell me your favorite movie", movies_df['title'].values)

# recommended = mv.recommend(movie)


# if st.button("Recommend"):

#     recommended = mv.recommend(movie)
#     cols = st.columns(3)

#     for idx, (_, row) in enumerate(recommended.iterrows()):

#         poster_url = fetch_poster(row["movie_id"])

#         with cols[idx % 3]:
#             if poster_url:
#                 st.image(poster_url, width = 75)
#             else:
#                 st.write("Poster not available")

#             st.write(row["title"])


# if __name__ == "__main__":
#     st.write("done")


import os
import sys
import streamlit as st

st.write("Current working directory:")
st.write(os.getcwd())

st.write("Root directory contents:")
st.write(os.listdir())

if "src" in os.listdir():
    st.write("SRC contents:")
    st.write(os.listdir("src"))

    if "movie_recommender" in os.listdir("src"):
        st.write("movie_recommender contents:")
        st.write(os.listdir("src/movie_recommender"))

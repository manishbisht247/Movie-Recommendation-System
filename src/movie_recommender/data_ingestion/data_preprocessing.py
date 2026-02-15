import pandas as pd
from movie_recommender.logger import logger
from movie_recommender.exceptions import CustomException


def collapse_names(lst):
    return [name.replace(" ", "") for name in lst]



def preprocess_movie_data(data:pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the movie data by creating a new 'tags' column that combines relevant information.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing movie data.

    Returns:
    pd.DataFrame: A transformed DataFrame with a new 'tags' column.
    """
    try:
        # Combine relevant columns into a single 'tags' column

        data['overview'] = data['overview'].apply(lambda x: x.split())
        logger.info("Split overview into list of words.")


        #collapse names
        cols = ['cast', 'crew', 'genres', 'keywords']

        for col in cols:
            data[col] = data[col].apply(collapse_names)
        logger.info("Collapsed names in cast, crew, genres, and keywords.")

        # Combine relevant columns into a single 'tags' column
        data['tags'] = data['genres'] + data['cast'] + data['overview'] + data['keywords'] + data['crew']
       
        # excluding other columns except movie_id, title and tags
        data = data.drop(columns=[col for col in data.columns if col not in ['movie_id', 'title', 'tags']])
        logger.info("Combined genres, cast, overview, keywords, and crew into 'tags' column.")
        
        # Select only the necessary columns for the recommendation system
        data = data[['movie_id', 'title', 'tags']]

        # convert into lowercase
        data['tags'] = data['tags'].apply(lambda x: [word.lower() for word in x])
        logger.info("Converted tags to lowercase.")
        
        return data
    except Exception as e:
        print(f"An error occurred during transformation: {e}")
        return pd.DataFrame()
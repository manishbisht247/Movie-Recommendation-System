import pandas as pd
from movie_recommender.logger import logger
from movie_recommender.exceptions import CustomException

def transform_movie_data(data:pd.DataFrame) -> pd.DataFrame:
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

        data['tags'] = data['overview'] + ' ' + data['genres'].apply(lambda x: ' '.join(x)) + ' ' + data['keywords'].apply(lambda x: ' '.join(x)) + ' ' + data['cast'].apply(lambda x: ' '.join(x)) + ' ' + data['crew'].apply(lambda x: ' '.join(x))
        
        # Select only the necessary columns for the recommendation system
        transformed_data = data[['movie_id', 'title', 'tags']]
        
        return transformed_data
    except Exception as e:
        print(f"An error occurred during transformation: {e}")
        return pd.DataFrame()
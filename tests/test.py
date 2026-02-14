from movie_recommender.data.fetch_data import fetch_movie_data
from movie_recommender.logger import logger
from movie_recommender.exceptions import CustomException
from movie_recommender.data.data_cleaning import Cleaning
from movie_recommender.data.data_preprocessing import transform_movie_data
if __name__ == "__main__":
    # Test fetching movie data
    try:
        movie_file = r"C:\Users\mbvin\OneDrive\Desktop\Movie-Recommendation-System\data\raw\tmdb_5000_movies.csv"
        credit_file = r"C:\Users\mbvin\OneDrive\Desktop\Movie-Recommendation-System\data\raw\tmdb_5000_credits.csv"
        movie_data, credit_data = fetch_movie_data(movie_file, credit_file)
        
        if not movie_data.empty and not credit_data.empty:
            logger.info("Movie data fetched successfully.")
            
        data = movie_data.merge(credit_data, on ='title')
        logger.info("Movie data merged successfully.")
                
        # Test data cleaning
        cleaning = Cleaning(data)
        cleaned_data = cleaning.full_cleaning()
        logger.info("Data cleaning completed successfully.")

        preprocessed_data = transform_movie_data(cleaned_data)
        logger.info("Data preprocessing completed successfully.")
        



    except Exception as e:
        print(f"Error fetching movie data: {e}")
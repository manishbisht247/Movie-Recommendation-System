from movie_recommender.logger import logger
from movie_recommender.exceptions import CustomException
from movie_recommender.data_ingestion.fetch_data import fetch_movie_data
from movie_recommender.data_ingestion.data_cleaning import Cleaning
from movie_recommender.data_ingestion.data_preprocessing import preprocess_movie_data
from movie_recommender.data_ingestion.data_transformation import DataTransformation



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

        # data preprocessing
        preprocessed_data = preprocess_movie_data(cleaned_data)
        logger.info("Data preprocessing completed successfully.")

        # Prepare preprocessed data for transformation
        preprocessed_data['text'] = preprocessed_data['tags'].apply(lambda x: " ".join(x))
        dtf = DataTransformation(preprocessed_data)
        final_data = dtf.full_transformation()
        logger.info("Data transformation completed successfully.")

    
        # export to data folder
        final_data.to_csv(r"C:\Users\mbvin\OneDrive\Desktop\Movie-Recommendation-System\data\preprocessed\final_data.csv", index=False)
        logger.info("Final data exported successfully.")


        




    except Exception as e:
        print(f"Error fetching movie data: {e}")

    except ModuleNotFoundError as m:
        print(f"module not found: {m}")
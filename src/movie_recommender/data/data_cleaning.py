# imports
from movie_recommender.logger import logger
from movie_recommender.exceptions import CustomException
import ast



# merging the two dataframes:


class Cleaning:

    def __init__(self, data):
        self.data = data

    def extract_columns(self):

        # extracting relevant columns for cleaning
        self.data = self.data[['movie_id','title','overview','genres','keywords','cast','crew']]
        logger.info("Selected relevant columns for cleaning.")
        return self.data
    
    def extract_cast(self, cast_data):
        # we have to find only top 3 casts:
        casts = []
        count = 0
        for i in ast.literal_eval(cast_data):
            if count!=3:
                casts.append(i['character'])
                count+=1
            else: break
        return casts
    
    def extract_crew(self, crew_data):
        director = []
        for i in ast.literal_eval(crew_data):
            if i['job'] == 'Director':
                director.append(i['name'])
        return director
    
    def extract_genres(self, genres_data):
        genres = []
        for i in ast.literal_eval(genres_data):
            genres.append(i['name'])
        return genres
    
    # for keywords, it is same as genres, so we can reuse the same function for keywords as well.

    def full_cleaning(self):
        self.data = self.extract_columns()
        logger.info("Extracted relevant columns for cleaning.")
        self.data['cast'] = self.data['cast'].apply(self.extract_cast)
        logger.info("Extracted top 3 casts.")
        self.data['crew'] = self.data['crew'].apply(self.extract_crew)
        logger.info("Extracted directors from crew.")
        self.data['genres'] = self.data['genres'].apply(self.extract_genres)
        logger.info("Extracted genres.")
        self.data['keywords'] = self.data['keywords'].apply(self.extract_genres)
        logger.info("Extracted keywords.")
        self.data = self.data.dropna()
        logger.info("Dropped rows with missing values.")
        return self.data

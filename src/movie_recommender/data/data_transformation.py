import re
import pandas as pd
from streamlit import text
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from movie_recommender.logger import logger
from movie_recommender.exceptions import CustomException

class DataTransformation:

    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def convert_to_string(self):
        # Convert the 'text' column to string type for all rows
        self.data['text'] = self.data['text'].astype(str)
        return self.data

    def remove_punctuation(self):
        # Remove punctuation from the 'text' column for all rows
        self.data['text'] = self.data['text'].apply(lambda x: re.sub(r"[^a-zA-Z\s]", " ", x))
        return self.data
    
    def clean_and_lemmatize(self):
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words("english"))
        custom_stop_words = set(["movie", "film", "actor", "actress", "director", "genre"])
        def process(text):
            return " ".join(
                lemmatizer.lemmatize(w)
                for w in text.split()
                if w not in stop_words and w not in custom_stop_words
            )
        self.data['text'] = self.data['text'].apply(process)
        return self.data
    
    def full_transformation(self):
        # Apply all transformations in sequence to self.data['text']
        self.convert_to_string()
        logger.info('converted to string')
        self.remove_punctuation()
        logger.info('removed punctuation')
        self.clean_and_lemmatize()
        logger.info('lemmatization done')
        return self.data
    
    

import requests
from movie_recommender.config import TMDB_API_KEY


API_KEY = TMDB_API_KEY
BASE_URL = "https://api.themoviedb.org/3/movie/"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

session = requests.Session()  # reuse connection



def fetch_poster(movie_id):

    url = f"{BASE_URL}{movie_id}?api_key={API_KEY}"

    try:
        response = session.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return IMAGE_BASE_URL + poster_path

        return None

    except requests.exceptions.RequestException:
        return None
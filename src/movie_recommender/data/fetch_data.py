import numpy as np
import pandas as pd

def fetch_movie_data(file_path1: str, file_path2: str) -> pd.DataFrame:
    """
    Fetch movie data from two CSV files.

    Parameters:
    file_path1 (str): The path to the first CSV file containing movie data.
    file_path2 (str): The path to the second CSV file containing movie credits data.

    Returns:
    pd.DataFrame: A DataFrame containing the movie data.
    """
    try:
        data1 = pd.read_csv(file_path1)
        data2 = pd.read_csv(file_path2)
        return data1, data2
    except FileNotFoundError:
        print(f"Error: The file at {file_path1 or file_path2} was not found.")
        return pd.DataFrame(), pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame(), pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame(), pd.DataFrame()
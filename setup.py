from setuptools import setup, find_packages
def read_requirements():
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()
setup(
    name="movie_recommender",
    version="0.1.0",
    description="Unified movie and series recommendation system",
    author="Manish",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements(),
)
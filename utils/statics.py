ROOT = "data/"

MOVIES_FILE = ROOT + "movies.csv"
RATINGS_FILE = ROOT + "ratings.csv"
LINKS_FILE = ROOT + "links.csv"
TAGS_FILE = ROOT + "tags.csv"

movie_id = "movie_id"
title = "title"
genres = "genres"
imdb_id = "imdb_id"
tmdb_id = "tmdb_id"
user_id = "user_id"
rating = "rating"
timestamp = "timestamp"
tag = "tag"

def genre_list(movies_list):
	return movies_list.split("|")

MOVIES_SCHEMA = ((movie_id, int),(title, str),(genres, genre_list))
LINKS_SCHEMA = ((movie_id, int),(imdb_id, str),(tmdb_id, str))
RATINGS_SCHEMA = ((user_id, int),(movie_id, int),(rating, float), (timestamp, int))
TAGS_SCHEMA = ((user_id, int),(movie_id, int),(tag, str), (timestamp, int))




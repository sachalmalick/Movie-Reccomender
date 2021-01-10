import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, neighbors
from sklearn.linear_model import LinearRegression
from scipy import spatial
from utils.data_preproc import *
from utils.statics import *

print("Loading data... This my take a couple of seconds")
movies, links, ratings, tags = get_all_data()
print("Complete!")

def compare_users(u1, u2):
	ratings_1 = get_ratings(u1, ratings)
	ratings_2 = get_ratings(u2, ratings)
	movies = [movie[movie_id] for movie in ratings_1]
	movies.extend(movie[movie_id] for movie in ratings_2)
	movies = set(movies)
	vector_1 = []
	vector_2 = []
	for movid in movies:
		vector_1.append(get_rating_for_movie(ratings_1, movid))
		vector_2.append(get_rating_for_movie(ratings_2, movid))
	return spatial.distance.cosine(vector_1, vector_2)


def predict(user, k=15):
	user_names = list(ratings.keys())
	if(user in user_names):
		user_names.remove(user)
	classifier = []
	for other_user in user_names:
		classifier.append(compare_users(user, other_user))
	user_names_arr = np.array(user_names)
	X_train = user_names_arr.reshape(len(user_names),1)
	y_train = np.array(classifier)
	model = neighbors.KNeighborsRegressor()
	model.fit(X_train, y_train)
	X_test = np.array([user]).reshape(1,1)
	neighbs = model.kneighbors(X_test,k,return_distance=False)
	neighbs = list(neighbs[0])
	neighbs = [user_names[i] for i in neighbs]
	return neighbs

def add_user(feedback):
	global ratings
	user_id = max(ratings.keys()) + 1
	ratings[user_id] = feedback
	return user_id

def rating_sort(movie):
	return movie[rating]
def get_movie_recs(neighbors):
	movie_recs = []
	for neighb in neighbors:
		user_ratings = ratings[neighb]
		user_ratings.sort(key=rating_sort)
		for movie in user_ratings:
			if(movie[rating] > 3):
				movie_recs.append(movie[movie_id])
	return movie_recs
def score_model(user):
	user_names = list(ratings.keys())
	if(user in user_names):
		user_names.remove(user)
	classifier = []
	for other_user in user_names:
		classifier.append(compare_users(user, other_user))
	user_names_arr = np.array(user_names)
	X = user_names_arr.reshape(len(user_names),1)
	y = np.array(classifier)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
	model = neighbors.KNeighborsRegressor()
	model.fit(X_train, y_train)
	score = model.score(X_test, y_test)
	print("Score: " + str(score))
"""
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
2,Jumanji (1995),Adventure|Children|Fantasy
3,Grumpier Old Men (1995),Comedy|Romance
4,Waiting to Exhale (1995),Comedy|Drama|Romance
5,Father of the Bride Part II (1995),Comedy
6,Heat (1995),Action|Crime|Thriller
7,Sabrina (1995),Comedy|Romance
8,Tom and Huck (1995),Adventure|Children
9,Sudden Death (1995),Action
10,GoldenEye (1995),Action|Adventure|Thriller

feedback = [{movie_id:1,rating:5}, {movie_id:2,rating:3}, {movie_id:3,rating:0}, {movie_id:4,rating:0}, {movie_id:5,rating:0}, {movie_id:6,rating:4}, {movie_id:7,rating:3}, {movie_id:8,rating:3}, {movie_id:9,rating:0},{movie_id:10,rating:5}]
new_user = add_user(feedback)
movie_recs = get_movie_recs(predict(new_user,k=10))
print(movie_recs)
"""
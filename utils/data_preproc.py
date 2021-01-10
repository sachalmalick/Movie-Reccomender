import utils.file_io as fio
from utils.statics import *

def type_data(dt, data):
	return dt(data)
def dic_from_schema(schema, data):
	dic = {}
	for i in range(len(data)):
		name = schema[i][0]
		dt = schema[i][1]
		dic[name] = type_data(dt, data[i])
	return dic
def create_dic(csv_data, schema):
	dic = {}
	for row in csv_data:
		try:
			key = schema[0]
			key = type_data(key[1], row[0])
			dic[key] =  dic_from_schema(schema[1:], row[1:])
		except Exception as e:
			continue
	return dic

def create_dic(csv_data, schema):
	dic = {}
	for row in csv_data:
		try:
			key = schema[0]
			key = type_data(key[1], row[0])
			dic[key] =  dic_from_schema(schema[1:], row[1:])
		except Exception as e:
			continue
	return dic

def create_dic_nested_list(csv_data, schema):
	dic = {}
	for row in csv_data:
		try:
			key = schema[0]
			key = type_data(key[1], row[0])
			value = dic_from_schema(schema[1:], row[1:])
			if(dic.get(key) == None):
				dic[key] = [value]
			else:
				dic[key].append(value)
		except Exception as e:
			continue
	return dic

def read_data(filename, schema, func=create_dic):
	data = fio.read_csv(filename)[1:]
	return func(data, schema)

def get_all_data():
	func = create_dic_nested_list
	movies = read_data(MOVIES_FILE, MOVIES_SCHEMA)
	links = read_data(LINKS_FILE, LINKS_SCHEMA)
	ratings = read_data(RATINGS_FILE, RATINGS_SCHEMA, func=func)
	tags = read_data(TAGS_FILE, TAGS_SCHEMA, func=func)
	return movies, links, ratings, tags

def get_ratings(user, ratings):
	return ratings[user]

def get_rating_for_movie(ratings, movid):
	for movie in ratings:
		if(movie[movie_id] == movid):
			return movie[rating]
	return 0
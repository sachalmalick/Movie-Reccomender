from flask import Flask, render_template, request,redirect,url_for,session
import random
from utils.learning import *
import json
import requests

app = Flask(__name__)
app.secret_key = 'password'
IMDB_KEY = "3df29fd2"
BASEURL = "http://www.omdbapi.com/?i=tt"
movie_list = []

def get_request_url(movid):
	return BASEURL + movid + "&apikey=" + IMDB_KEY

def decode_movie_json(url):
	response = requests.get(url)
	response = response.json()
	return dict(response)

def random_ten():
	sample = random.sample(list(movies.keys()), 12)
	l = [(i, links[i][imdb_id]) for i in sample]
	return l

def get_movie_data(movies):
	movie_data = []
	for movie in movies:
		imdb = movie[1]
		url = get_request_url(imdb)
		movie_data.append(decode_movie_json(url))
	return movie_data

def get_ratings(feedback):
	rated_feedback = []
	total = 0
	for i in range(0, len(feedback)):
		if((i % 5) == 0 and (i > 0)):
			rated_feedback.append(total)
			total = 0
		if(feedback[i] == "true"):
			total+=1
	rated_feedback.append(total)
	return rated_feedback

def rated_feedback_to_user(feedback):
	user = []
	for i in range(0, len(feedback)):
		dic = {}
		dic[rating] = feedback[i]
		dic[movie_id] = movie_list[i][0]
		user.append(dic)
	return user



@app.route("/", methods = ['GET', 'POST'])
def mainpage():
	global movie_list
	movie_list=random_ten()
	movie_data=get_movie_data(movie_list)
	return render_template("index.html", movies=movie_data)

@app.route("/suggestions", methods = ['GET', 'POST'])
def suggest():
	feedback = request.args.get('feedback')
	feedback = feedback.split(",")
	feedback = get_ratings(feedback)
	user = rated_feedback_to_user(feedback)
	user_id = add_user(user)
	movie_recs = get_movie_recs(predict(user_id,k=10))
	already_shown = [i[0] for i in movie_list]
	movie_recs = [i for i in movie_recs if not i in already_shown]
	movie_recs = movie_recs[:12]
	movie_recs = [(i, links[i][imdb_id]) for i in movie_recs]
	movie_recs = get_movie_data(movie_recs)
	return render_template("recs.html", movies=movie_recs)

@app.route("/test", methods = ['GET', 'POST'])
def test():
	return render_template("test.html")


if __name__=="__main__":
    app.run("localhost", 5000, debug = True)

	
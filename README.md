# This is the Twitter_Scrapper by Adrian Trzoss. App that connetcts to Twitter API via Tweepy library and gets Twitter User's Timeline of tweets that later could be used during some data mining.

# Contents:

1. Project Summary:
	a) Introduction
	b) Methods
	c) Used technology and methods
2. Setup
3. Algorithm step by step
4. Known issues
5. Info about contributor

# 1. Project Summary:

	# a) Introduction
		The Twitter_scraper by Adrian Trzoss is the program that uses the Tweepy library to get Tweets from Twitter API. Currently it contains two modules: API and analysis module. Project was implemented with Python Programming Language 3.7 with Anaconda Env. using following libs: tweepy, json, datetime, pandas, numpy, matplotlib, re, nltk, pyplot (as for 1.07.2019). Project is under development - version 0.2 'Scipio'.

	# b) Methods
		Program starts with several functions: API - requires from user to have a Developer Twitter Account, Register APP and generate 4 access keys that should be filled in the code; Program can either gets own tweets and metadata or another User's; finally both are exported with preselected TweetClass atributes to json file (such as id, created time, text, source, retweet and favorite count, if is retweet or original tweet).
		Analizy.py uses generated json file given by the user in setup function. Currently two methods are available - getting statistics for retweet_count and figure generator of retweet count in time.

	# c) Used technology and methods
		The project was developed with the usage of Python 3.7.3 with the PyCharm IDE on Anaconda packages - tweepy, json, datetime, pandas, numpy, matplotlib, re, nltk, pyplot (as for 1.07.2019)

# 2. Setup

	Currently program operates on systems with Python 3.7.3. Suggested package Anaconda or Pycharm.

# 3. Algorithm step by step

	Program starts with consumer key and secret key, access token and secret token empty - to be given by user.
	Program combines all four keys into authentication request to be sent to API (tweepy.API(auth)).
	Function: get my tweets returns list of own public tweets.
	Function: get my metadata returns user own Twitter name, followers count and friends' names.
	Function: get user tweets starts with an empty list and asks to give twitter account name and how many RECENT tweets would user like to collect. Than returns tweets and add(extend) them to empty list. For each tweet in the list function will iterate and return preselected atributes (params): id, created date, full text, source, retweet count, favorite count, if is retweet. Than return username collected and new list of tweets.
	Function: Output tweets to json creates empty dictionary that is fullfiled with data from the list. Dict will be changed into json file and save in the directory. 

	ANALYSIS Function: setup gets from user the json filename to be used as a working file.
	ANALYSIS Function: stats for retweets: uses working file to get list of stats for retweet count: mean, sum, median, std, max, min. Returns list of stats.
	ANALYSIS Function: uses working file to set index on created_at (date) param. While using pyplot creates figure (png) of retweet count in time and saves into directory.


# 4. Known issues & Further development
	
	Currently get tweets retruns max 3200 tweets dure to Twitter API limits.
	Next step is to pass the limit of tweets to get, collect tweets by hashtags.
	In analysis module: ngram module to be implemented and create fuctions to get variables not static params.
	Unittests are expected in near future.

# 5. Info about contributor.

	Development: Adrian Trzoss MA. PhD candidate at Faculty of History at Adam Mickiewicz University (AMU) in Poznan. Beginner in Python world. Great fun of oldschool rock music and tasty cooking.

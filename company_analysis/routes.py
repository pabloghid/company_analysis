from company_analysis import app
from flask import render_template
import snscrape.modules.twitter as sntwitter

class Tweet():
    def __init__(self, date, url, content):
        self.date = date
        self.url = url
        self.content = content

@app.route('/')
@app.route('/index')
def index():
    max_tweets = 10
    i = 0
    tweets_list = []
    scraper = sntwitter.TwitterSearchScraper("Futemax since:2023-06-06 until:2023-06-13")
    for tweet in scraper.get_items():
        if i > max_tweets:
            break
        tweets_list.append(Tweet(tweet.date, tweet.url, tweet.content))

    return render_template('list.html', tweets=tweets_list)
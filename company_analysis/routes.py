from .models.Tweet import Tweet
from . import app
from flask import render_template, request
import snscrape.modules.twitter as sntwitter

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        nome_empresa = request.form.get('nome_empresa')
        ## TODO: pegar request de max_tweets, since-until, limits e outros filtros
        max_tweets = 10
        i = 0
        tweets_list = []
        scraper = sntwitter.TwitterSearchScraper(nome_empresa + " since:2023-06-13 until:2023-06-20")
        for tweet in scraper.get_items():
            if i > max_tweets:
                break
            tweets_list.append(Tweet(tweet.date, tweet.url, tweet.content))
            i+=1

        return render_template('list.html', tweets=tweets_list)
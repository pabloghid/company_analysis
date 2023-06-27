from . import app
from flask import render_template, request, redirect
import snscrape.modules.twitter as sntwitter
from . import analyser
from .models.Tweet import Tweet
from .utils import convert_date

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/saibamais')
def saibamais():
    return render_template('paginaexplicativa.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        since_date = request.form.get('since_date')
        until_date = request.form.get('until_date')
        tweet_quantity = int(request.form.get('tweet_quantity'))

        max_tweets = tweet_quantity
        i = 0
        tweets_list = []
        tweets_details = []
        
        scraper = sntwitter.TwitterSearchScraper(company_name + " since:" + since_date + " until:" + until_date)
        for tweet in scraper.get_items():
            if i > max_tweets:
                break
            tweets_list.append(tweet.content)
            tweets_details.append(Tweet(tweet.date, tweet.url, tweet.content))
            i+=1
        
        analysis = analyser.analyser(tweets_list)
        since_date=convert_date(since_date)
        until_date=convert_date(until_date)
        
        return render_template('list.html', tweets=tweets_list, tweets_details=tweets_details, 
                               analysis=analysis, company_name=company_name, since=since_date, until=until_date, tweet_quantity=tweet_quantity)
    
    elif request.method == 'GET':
        return redirect("index")
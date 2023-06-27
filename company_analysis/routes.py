from . import app
from flask import render_template, request, redirect
import snscrape.modules.twitter as sntwitter
from . import analyser
from .models.Tweet import Tweet

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        ## TODO: pegar request de max_tweets, since-until, limits e outros filtros
        max_tweets = 30
        i = 0
        tweets_list = []
        tweets_details = []
        scraper = sntwitter.TwitterSearchScraper(company_name + " since:2023-06-13 until:2023-06-20")
        for tweet in scraper.get_items():
            if i > max_tweets:
                break
            tweets_list.append(tweet.content)
            ## tweet.date formatar para data
            tweets_details.append(Tweet(tweet.date, tweet.url, tweet.content))
            i+=1
        analysis = analyser.analyser(tweets_list)
        return render_template('list.html', tweets=tweets_list, tweets_details=tweets_details, analysis=analysis, company_name=company_name)
    
    elif request.method == 'GET':
        return redirect("index")
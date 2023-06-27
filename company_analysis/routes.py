from . import app
from flask import render_template, request, redirect
import snscrape.modules.twitter as sntwitter
from .analyzer import analyzer
from .models.Tweet import Tweet
from .utils import convert_date, tweets_by_day

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
        
        analysis = analyzer(tweets_list)
        since_date=convert_date(since_date)
        until_date=convert_date(until_date)

        # Analisar tweets por dia
        tweets_day = tweets_by_day(tweets_details)
        tweets_day_analyzed = {}
        days = []
        positive =[]
        negative = []
        neutral = []
        for day in tweets_day:
            analyze_day = analyzer(tweets_day[day])
            days.append(day)
            positive.append(analyze_day['positive'])
            negative.append(analyze_day['negative'])
            neutral.append(analyze_day['neutral'])
            tweets_day_analyzed[day] = analyze_day

        print(tweets_list)
        print(tweets_details)

        return render_template('list.html', tweets=tweets_list, tweets_details=tweets_details, positive=positive, negative=negative, neutral=neutral,
                               days=days, analysis=analysis, company_name=company_name, since=since_date, until=until_date, tweet_quantity=tweet_quantity)
    
    elif request.method == 'GET':
        return redirect("index")
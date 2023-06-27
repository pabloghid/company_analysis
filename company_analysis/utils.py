from datetime import datetime
def convert_date(date):
    date_obj = datetime.strptime(str(date), "%Y-%m-%d")
    converted_date = date_obj.strftime("%d/%m/%Y")
    return(converted_date)

def tweets_by_day(tweets):
    
    tweets_by_day = {}

    for tweet in tweets:
        day = tweet.date

        if day not in tweets_by_day:
            tweets_by_day[day] = []

        tweets_by_day[day].append(tweet.content)

    return(tweets_by_day)
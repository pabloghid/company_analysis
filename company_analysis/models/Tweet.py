from datetime import datetime

class Tweet():
    def __init__(self, date, url, content):
        self.url = url
        self.content = content
        date_obj = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S%z")
        formatted_date = date_obj.strftime("%d/%m/%Y")
        self.date = formatted_date
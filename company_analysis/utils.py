from datetime import datetime
def convert_date(date):
    date_obj = datetime.strptime(str(date), "%Y-%m-%d")
    converted_date = date_obj.strftime("%d/%m/%Y")
    return(converted_date)

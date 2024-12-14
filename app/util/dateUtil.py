from datetime import datetime

def getDate_Now() -> str:
    return formatDate(datetime.now())

def formatDate(_date: datetime) -> str:
    # Format the datetime object to a string
    formatted_date = _date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date
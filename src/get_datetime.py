from datetime import datetime

def get_datetime():
    #Get current time
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    return timestamp

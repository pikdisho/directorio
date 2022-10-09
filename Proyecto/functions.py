from datetime import date, time, datetime
def hora():
    return datetime.now().strftime('%H:%M:%S')

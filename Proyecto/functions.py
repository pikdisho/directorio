from datetime import date, time, datetime
def hora_completa():
    return datetime.now().strftime('%H:%M:%S')

def hora_sola():
    return (int(datetime.now().strftime('%H')))

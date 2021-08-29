import datetime

def TimeOfDay(user_sir=True):
    hour = int(datetime.datetime.now().hour)
    
    
    if hour >= 0 and hour < 12:
        text = "Good morning."
    elif hour >= 12 and hour < 18:
        text = "Good afternoon."
    else:
        text = "Good evening."
    
    if user_sir:
        text = text.replace(".", ", sir.")
    return text
from datetime import datetime

def greet(name):
    message = ''
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    message += ', ' + name + '-san!'
    print(message)




greet('Inoue')

# wishes/views.py
from django.shortcuts import render
import datetime

def wish_user(request):
    current_time = datetime.datetime.now()
    hour = current_time.hour
    message = ""

    if hour < 12:
        message = "Good morning."
    elif 12 <= hour < 17:
        message = "Good afternoon."
    else:
        message = "Good evening."

    return render(request, 'wishes/wish.html', {'message': message})

from django.shortcuts import render
import random

def home(request):
    quotes = [
        "Keep going, you're doing great!",
        "Believe in yourself.",
        "One step at a time.",
        "Stay positive, work hard, make it happen.",
        "Don’t stop until you’re proud."
    ]

    random_colors = {
        "Red": "red",
        "Orange": "orange",
        "Yellow": "yellow",
        "Green": "green",
        "Blue": "blue",
        "Indigo": "indigo",
        "Violet": "violet",
    }

    selected_quote = None
    selected_color = None

    if request.method == "POST":
        selected_color = request.POST.get("color")
        selected_quote = random.choice(quotes)

    return render(request, 'app_one/home.html', {
        "quote": selected_quote,
        "color": selected_color,
        "colors": random_colors
    })

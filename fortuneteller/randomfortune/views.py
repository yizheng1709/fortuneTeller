from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {'fortune': fortune}
    return render(request, 'randomfortune/fortune.html', context)

fortuneList = [
    "A pleasant surprise is waiting for you.",
    "Good things come to those who wait.",
    "Your talents will be recognized and rewarded.",
    "An exciting opportunity is on the horizon.",
    "Believe in yourself and all that you are.",
    "Your dreams are within reach; go for them.",
    "A new friendship will enrich your life.",
    "Luck is on your side today.",
    "Your future is looking bright and promising.",
    "Success is in your near future.",
    "A joyful and fulfilling journey awaits you.",
    "You will find love and happiness soon.",
    "Your hard work will pay off in the long run.",
    "Take risks and great rewards will follow.",
    "The best way to predict the future is to create it.",
    "A prosperous and fulfilling career is in your future.",
    "You will overcome any obstacles that come your way.",
    "Adventure awaits you just around the corner.",
    "Your positive attitude will lead to success.",
    "You are destined to make a difference.",
    "A happy surprise is coming your way.",
    "New opportunities will come knocking on your door.",
    "Embrace change; it will lead you to great things.",
    "Your determination will lead you to triumph.",
    "Happiness is a choice; choose it every day.",
    "You have the power to create your own destiny.",
    "Trust your instincts; they will guide you well.",
    "Love and laughter will fill your life.",
    "Your efforts will be rewarded abundantly.",
    "Stay focused, and you will achieve greatness.",
    "Good fortune will follow you wherever you go."
]
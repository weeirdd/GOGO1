import requests
from .models import City
from .forms import CityForm
from django.shortcuts import render
import sqlite3
from django.http import HttpResponse


def index(request):
    appid = 'df1a063efe9704a0693d95fc88b6c922'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"],
            'feels': response["main"]["feels_like"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def weekweather(request):
    return render(request, 'weather/weekweather.html')


def outfits(request):
    if request.method == 'POST':
        weather = request.POST.get("weather")
        mood = request.POST.get("mood")
        classic = request.POST.get("classic")
        casual = request.POST.get("casual")
        sport = request.POST.get("sport")
        glamour = request.POST.get("glamour")
        retro = request.POST.get("retro")
    else:
        return render(request, "weather/outfits.html")

    db = sqlite3.connect('WeatherGogo\gogo_db.sqlite3')
    c = db.cursor()
    select_query = "SELECT * FROM answers"
    c.execute(select_query)
    # result = c.fetchall()
    # print(result)
    c.execute(f'''INSERT INTO answers (weather, mood, classic, casual, sport, glamour, retro ) 
    VALUES ("{weather}", {mood}, "{classic}", "{casual}", "{sport}", "{glamour}", "{retro}")''')

    images = ["https://i.imgur.com/IKV42LS.jpg", "https://imgur.com/VnuYTV1.jpg", "https://i.imgur.com/MwUIXOc.jpg",
              "https://i.imgur.com/GhzWonD.jpg", "https://i.imgur.com/ZzVZrGB.jpg", "https://i.imgur.com/GWlRRSo.jpg",
              "https://i.imgur.com/SHwHl8M.jpg", "https://i.imgur.com/GneFMau.jpg", "https://i.imgur.com/ZrpxdSW.jpg",
              "https://i.imgur.com/O92cY5Q.jpg", "https://i.imgur.com/UGVMXBQ.jpg", "https://i.imgur.com/2qo0aAQ.jpg",
              "https://i.imgur.com/ZrpxdSW.jpg", "https://i.imgur.com/SHwHl8M.jpg", "https://i.imgur.com/y4T0xB3.jpg",
              "https://i.imgur.com/JbnPzRp.jpg", "https://i.imgur.com/SOGmpLd.jpg", "https://i.imgur.com/iZ715mm.jpg",
              "https://i.imgur.com/55sEIaY.jpg", "https://i.imgur.com/x2BRoQ8.jpg", "https://i.imgur.com/yjTD3L1.jpg",
              "https://i.imgur.com/COitb2M.jpg"
              ]


    if 0 < int(weather) <= 15 and casual == "on":
        context = {'image_0': images[0], 'image_7': images[7]}
    elif -10 < int(weather) <= 0 and casual == "on":
        context = {'image_5': images[5], 'image_4': images[6]}
    elif -20 <= int(weather) <= -10 and casual == "on":
        context = {'image_4': images[4], 'image_3': images[3]}
    elif 0 < int(weather) <= 15 and glamour == "on":
        context = {'image_2': images[2], 'image_1': images[1]}
    elif -10 < int(weather) <= 0 and classic == "on":
        context = {'image_8': images[14], 'image_9': images[9]}
    elif 0 < int(weather) <= 15 and classic == "on":
        context = {'image_10': images[10], 'image_11': images[11]}
    elif -10 <= int(weather) < 0 and sport == "on":
        context = {'image_12': images[12], 'image_13': images[13]}
    elif 0 <= int(weather) <= 15 and sport == "on":
        context = {'image_8': images[8], 'image_15': images[15]}
    elif 0 <= int(weather) <= 15 and retro == "on":
        context = {'image_16': images[16], 'image_17': images[17]}
    elif -10 < int(weather) <= 0 and glamour == "on":
        context = {'image_18': images[18], 'image_19': images[19]}
    elif -10 <= int(weather) < 0 and retro == "on":
        context = {'image_20': images[20], 'image_21': images[21]}
    db.commit()
    db.close()

    return render(request, 'weather/casual.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        age = request.POST.get("age")
        email = request.POST.get("email")
        password = request.POST.get("password")
    else:
        print(20)
        return render(request, "weather/register.html")

    db = sqlite3.connect('WeatherGogo\gogo_db.sqlite3')
    c = db.cursor()
    select_query = "SELECT * FROM user"
    c.execute(select_query)
    result = c.fetchall()
    print(result)
    c.execute(f'''INSERT INTO user (username, age, email, password) VALUES ("{username}", {age}, "{email}", "{password}")''')
    db.commit()
    db.close()
    return render(request, 'weather/register.html')

def support(request):
    return render(request, 'weather/support.html')

def feedback(request):
    return render(request, 'weather/feedback.html')

def readyout(request):
    return render(request, 'weather/readyout.html')

def looks(request):
    return render(request, 'weather/looks.html')

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WeatherGogo.urls')),
    path('week/', include('WeatherGogo.urls')),
    path('outfits/', include('WeatherGogo.urls')),
    path('register/', include('WeatherGogo.urls')),
    path('support/', include('WeatherGogo.urls')),
    path('feedback/', include('WeatherGogo.urls')),
    path('ready/', include('WeatherGogo.urls')),
    path('looks/', include('WeatherGogo.urls'))
]


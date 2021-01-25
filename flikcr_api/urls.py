from django.urls import path

from . import views

urlpatterns = [

    path('searchPresets/', views.index, name='searchPresets'),
    path('searchByLatAndLon/',views.searchLatLon, name='searchLatLon'),
    path('searchCities/', views.searchCities, name='searchCities'),
    path('favourites/', views.favourites, name='fav'),
    path('addPreset/', views.add, name='add'),
    path('', views.index, name='searchPresets'),

]

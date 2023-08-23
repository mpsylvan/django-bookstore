from django.urls import path
from .views import formatted_results, home

app_name = 'sales'

urlpatterns = [
    path('', home),
    path('binkies', formatted_results)
]
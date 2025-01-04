from django.urls import path
from . import views


app_name = 'weather'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('result_search/', views.search_result, name='search'),
    path('delete/', views.delete_forecast, name='delete'),
]

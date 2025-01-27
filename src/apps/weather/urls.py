from django.urls import path
from . import views


app_name = 'weather'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('result_search/', views.SearchResultView.as_view(), name='search'),
    path('delete/', views.DeleteLocationView.as_view(), name='delete'),
]

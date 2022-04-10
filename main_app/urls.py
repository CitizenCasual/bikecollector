from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bikes/', views.bikes_index, name='bikes_index'),
  path('bikes/<int:bike_id>/', views.details, name='details'),
  path('bikes/create/', views.BikeCreate.as_view(), name='bikes_create')
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bikes/', views.bikes_index, name='bikes_index'),
  path('bikes/<int:bike_id>/', views.details, name='details'),
  path('bikes/create/', views.BikeCreate.as_view(), name='bikes_create'),
  path('bikes/<int:pk>/update/', views.BikeUpdate.as_view(), name='bikes_update'),
  path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bikes_delete'),
  path('bikes/<int:bike_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('tools/create/', views.ToolCreate.as_view(), name='tools_create'),
  path('tools/<int:pk>/', views.ToolDetail.as_view(), name='tool_detail'),
  path('tools/', views.ToolList.as_view(), name='tool_list'),
]
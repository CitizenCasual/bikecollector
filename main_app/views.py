from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bike


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', { 'bikes': bikes })

def details(request, bike_id):
  bikes = Bike.objects.get(id=bike_id)
  return render(request, 'bikes/details.html', { 'bike': bikes })


class BikeCreate(CreateView):
  model = Bike
  fields = '__all__'

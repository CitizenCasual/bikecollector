from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.forms import MaintenanceForm
from .models import Bike, Tool
from .forms import MaintenanceForm


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
  maintenance_form = MaintenanceForm()
  return render(request, 'bikes/details.html', { 'bike': bikes, 'maintenance_form': maintenance_form })

def add_maintenance(request, bike_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.bike_id = bike_id
    new_maintenance.save()
  return redirect('details', bike_id=bike_id)
class BikeCreate(CreateView):
  model = Bike
  fields = '__all__'

class BikeUpdate(UpdateView):
  model = Bike
  fields = ['type', 'make', 'description']

class BikeDelete(DeleteView):
  model = Bike
  success_url = '/bikes/'

class  ToolCreate(CreateView):
  model = Tool
  fields = '__all__'

class ToolList(ListView):
  model = Tool

class ToolDetail(DetailView):
  model = Tool
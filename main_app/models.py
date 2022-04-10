from django.db import models
from django.urls import reverse

# Create your models here.

TYPES = (
  ('Mountain', 'Mountain'),
  ('Road', 'Road'),
  ('Gravel', 'Gravel'),
)

TASKS = (
  ('LC', 'Lube Chain'),
  ('WF', 'Wash Frame'),
  ('FT', 'Fill Tires'),
  ('CB', 'Check Bearings'),
  ('RB', 'Replace Brake Pads'),
  ('BW', 'Balance Wheels')
)
class Bike(models.Model):
  type = models.CharField(max_length=8, choices=TYPES, default=TYPES[0])
  make = models.CharField(max_length=25)
  model = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  year = models.IntegerField()

  def __str__(self):
    return self.make

  def get_absolute_url(self):
      return reverse("details", kwargs={"bike_id": self.id})

class Maintenance(models.Model):
  date = models.DateField('Maintenance date')
  task = models.CharField(max_length=2, choices=TASKS, default=TASKS[0][0])
  bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_task_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']
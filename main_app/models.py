from django.db import models

# Create your models here.

TYPES = (
  ('Mountain', 'Mountain'),
  ('Road', 'Road'),
  ('Gravel', 'Gravel'),
)
class Bike(models.Model):
  type = models.CharField(max_length=8, choices=TYPES, default=TYPES[0])
  make = models.CharField(max_length=25)
  model = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  year = models.IntegerField()

  def __str__(self):
    return self.make
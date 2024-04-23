from django.db import models
from django.urls import reverse

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=350)
  age = models.IntegerField()

  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})
    # Instance method, take reference to the instance
  
class Feeding(models.Model):
  MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
  )
  date = models.DateField('feeding date')
  meal = models.CharField(max_length=1, choices=MEALS)
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
  # takes the model its referencing and an on_delete argument
  # 

  def __str__(self):
    return f'{self.get_meal_display()} on {self.date}'
  # get_xyz_display will return the values with the keys from our MEALS tuples
  # used on fields that contain choices

  class Meta:
    ordering = ('-date',)
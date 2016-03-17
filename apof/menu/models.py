from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 128)
	open_hours = models.CharField(max_length = 64)
	phone_number = models.CharField(max_length = 64)
	slug = models.SlugField(unique=True)
	
	def __str__(self):
		return (self.name)
		
class Ingredient(models.Model):
	name = models.CharField(max_length = 128)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	
	def __str__(self):
		return (self.name)
		
class Menu(models.Model):
	dish = models.CharField(max_length = 128)
	restaurant = models.ForeignKey(Restaurant)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	ingredients = models.ManyToManyField(Ingredient)
	size = models.CharField(max_length = 64)
	rating = models.IntegerField()
	rating_description = models.CharField(max_length = 512)
	
	def __str__(self):
		return (self.dish)
		
#class Cart(models.Model):
	

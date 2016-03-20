from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 128)
	open_hour = models.CharField(max_length = 16)
	close_hour = models.CharField(max_length = 16)
	address = models.CharField(max_length = 128)
	delivery_time = models.CharField(max_length = 16)
	phone_number = models.CharField(max_length = 64)
	slug = models.SlugField(unique=True)
	
	def __str__(self):
		return self.name
		
class Ingredient(models.Model):
	name = models.CharField(max_length = 128)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	
	def __str__(self):
		return self.name
		
class Menu(models.Model):
	dish = models.CharField(max_length = 128)
	restaurant = models.ForeignKey(Restaurant)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	ingredients = models.ManyToManyField(Ingredient)
	size = models.CharField(max_length = 64)
	rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
	rating_description = models.CharField(max_length = 512)
			
	def __str__(self):
		return self.dish 
	#def menu_restaurant(self):
	#	return self.restaurant
		
class Cart(models.Model):
	user = models.CharField(max_length=64)
	date = models.CharField(max_length=32)
	dish = models.ForeignKey(Menu)
	#dish = models.CharField(max_length = 128)
	restaurant = models.CharField(max_length = 128)

	def __str__(self):
		return self.dish

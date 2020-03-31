from django.db import models

# Create your models here.

# database file


# all you have to do is write a class 

# the database is abstracted from the code. 

class Stock(models.Model):

	ticker = models.CharField(max_length=20)

	def __str__(self):
		# this is for the admin area
		return self.ticker
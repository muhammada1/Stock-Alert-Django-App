from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WatchList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist", null=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Stock(models.Model):
	watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()
	target = models.IntegerField(max_length=10)

	def __str__(self):
		return self.text
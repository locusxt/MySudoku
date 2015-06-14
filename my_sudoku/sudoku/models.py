from django.db import models

# Create your models here.
class GameLog(models.Model):
	question = models.CharField(max_length = 81)
	level = models.CharField(max_length = 10)
	player = models.CharField(max_length = 64)
	cost_time = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
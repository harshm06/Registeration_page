from django.db import models

# Create your models here.

class details(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	address=models.CharField(max_length=300)
	city=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	zip1=models.IntegerField()
	board=models.CharField(max_length=100)
	qualified=models.CharField(max_length=100)
	mobileno = models.IntegerField()
	email = models.CharField(max_length=100)
	gender=models.CharField(max_length=20)
	
	
class user(models.Model):
	link=models.ForeignKey(details, on_delete=models.CASCADE)
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

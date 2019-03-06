from django.db import models
from django.contrib.auth.models import User
from multi_email_field.fields import MultiEmailField

# Create your models here.
class Country(models.Model):
	name =models.CharField(max_length=30)

class Channel(models.Model):
	name =models.CharField(max_length=60)

class Researchment(models.Model):
	name = models.CharField(max_length=40)


class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

class Client(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

class Cycle(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	researchment = models.ForeignKey(Researchment, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	order = models.IntegerField()


class Request(models.Model):
	name =models.CharField(max_length=30)


		
class Transaction(models.Model):
	type_requiriment = models.CharField(max_length=150)
	priority = models.CharField(max_length=2)
	request = models.ForeignKey(Request, on_delete=models.CASCADE)
	description = models.TextField()
	copy = MultiEmailField()
	attached = models.FileField(upload_to='folder/')
	request_status = models.BooleanField(null = True)
	deadline = models.DateTimeField()
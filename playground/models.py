from django.db import models

# Create your models here.

class Pet (models.Model):
    name = models.CharField(max_length=75)
    species = models.CharField(max_length=10)
    breed = models.CharField(max_length=25)
    age = models.IntegerField()
    picture = models.CharField(max_length=1000)
    adoption_status = models.ForeignKey('Adoption_status', on_delete=models.SET_NULL, null=True)

class Adoption_status (models.Model):
    status = models.CharField(max_length=25)
    adopted_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True , blank=True) 
    adoption_date= models.DateField(max_length=20 , null=True ,blank=True)
    notes= models.CharField(max_length=1000)

class user (models.Model) :
    name = models.CharField (max_length=40)
    age = models.IntegerField()
    work = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

class volunteer (models.Model) :
    name = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    free_hours_a_week= models.IntegerField()
    exprtise = models.TextField(max_length=750)


class medical_history (models.Model) :
    medical_history_for_the_pet = models.CharField(max_length=350)
    current_health_status = models.CharField(max_length=350)
    vaccinations = models.CharField(max_length=75)
    on_going_medication = models.CharField(max_length=350)



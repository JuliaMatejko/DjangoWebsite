from django.db import models

class Species(models.Model):
    species = models.CharField(max_length=50)

class Breed(models.Model):
    breed = models.CharField(max_length=50)

class Sex(models.Model):
    sex = models.BooleanField()

class Size(models.Model):
    size = models.CharField(max_length=30)


class BasicInfoCard(models.Model):
    name = models.CharField(max_length=50)
    date_of_registration = models.DateTimeField('date registered')
    species = models.ForeignKey(Species, on_delete=models.RESTRICT)
    breed = models.ForeignKey(Breed, on_delete=models.RESTRICT)
    sex = models.ForeignKey(Sex, on_delete=models.RESTRICT)
    age = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.RESTRICT)


class DetailInfoCard(models.Model):
    basic_info_card = models.ForeignKey(BasicInfoCard, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)





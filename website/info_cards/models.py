from django.db import models
from django.utils import timezone

class Species(models.Model):
    species = models.CharField(max_length=50)

    def __str__(self):
        return self.species


class Breed(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed


class Sex(models.Model):
    sex = models.CharField(max_length=20)

    def __str__(self):
        return self.sex


class Size(models.Model):
    size = models.CharField(max_length=30)

    def __str__(self):
        return self.size


class BasicInfoCard(models.Model):
    name = models.CharField(max_length=50)
    date_of_registration = models.DateTimeField('date registered')
    species = models.ForeignKey(Species, on_delete=models.RESTRICT)
    breed = models.ForeignKey(Breed, on_delete=models.RESTRICT)
    sex = models.ForeignKey(Sex, on_delete=models.RESTRICT)
    age = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.name}, {self.date_of_registration}, {self.species}, {self.breed}, {self.sex}, {self.age}, {self.size}'

    def was_added_recently(self):
        return self.date_of_registration >= timezone.now() - datetime.timedelta(days=1)

class DetailInfoCard(models.Model):
    basic_info_card = models.ForeignKey(BasicInfoCard, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.description




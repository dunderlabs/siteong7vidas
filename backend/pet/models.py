from django.db import models


class PetBreed(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "PetBreed"
        verbose_name_plural = "PetsBreed"

    def __str__(self):
        return self.name


class Pet(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    age = models.DateField()
    adoted = models.BooleanField()
    race = models.CharField(max_length=50)
    pelage = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    def __str__(self):
        return self.name

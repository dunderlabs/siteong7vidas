from django.db import models


class PetBreed(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "PetBreed"
        verbose_name_plural = "PetsBreed"

    def __str__(self):
        return self.name


class Pet(models.Model):

    PET_TYPE_CHOICES = (
        ('cat', 'cat'),
        ('dog', 'dog'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    age = models.DateField()
    is_adopted = models.BooleanField()
    is_castrated = models.BooleanField()
    breed = models.ForeignKey(PetBreed, on_delete=models.CASCADE)
    pelage = models.CharField(max_length=50)
    _type = models.CharField(
        max_length=10,
        choices=PET_TYPE_CHOICES
    )

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    @property
    def type(self):
        return self._type

    def __str__(self):
        return self.name

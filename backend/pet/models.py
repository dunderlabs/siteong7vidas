from django.db import models
from django.utils.text import slugify
from django.urls import reverse as r


class PetBreed(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = "PetBreed"
        verbose_name_plural = "PetsBreed"

    def save(self):
        self.slug = slugify(self.name)

        super(PetBreed, self).save()

    def __str__(self):
        return self.name


class PetPelage(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Pelage"
        verbose_name_plural = "Pelages"

    def save(self):
        self.slug = slugify(self.name)

        super(PetPelage, self).save()

    def __str__(self):
        return self.name


class Pet(models.Model):

    PET_TYPE_CHOICES = (
        ('cat', 'cat'),
        ('dog', 'dog'),
    )

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    is_adopted = models.BooleanField(default=False)
    is_castrated = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='images/uploads',
        default='images/uploads/default.png',
        blank=True
    )
    breed = models.ForeignKey(
        PetBreed,
        related_name='pets',
        related_query_name='pet',
        on_delete=models.CASCADE
    )
    pelage = models.ForeignKey(
        PetPelage,
        on_delete=models.CASCADE
    )
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

    def get_absolute_url(self):
        return r('pet:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

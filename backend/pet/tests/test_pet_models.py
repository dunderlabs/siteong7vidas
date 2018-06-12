from django.test import TestCase
from django.conf import settings
from model_mommy import mommy
from backend.pet.models import Pet, PetBreed, PetPelage


class PetTestModel(TestCase):

    def setUp(self):
        self.pet = mommy.make(Pet)

    def test_string_representation(self):
        self.assertIsInstance(str(self.pet), str)

    def test_pet_type_property(self):
        pet_types = [pet_type for pet_type, index in self.pet.PET_TYPE_CHOICES]

        self.assertIn(self.pet.type, pet_types)

    def test_pet_slug(self):
        self.pet.name = 'Abigodal'
        self.pet.save()

        self.assertEquals(self.pet.slug, 'abigodal')

    def test_pet_breed_foreign_attr(self):
        self.pet.breed.name = 'Bulldog'
        self.pet.breed.save()

        self.assertIsInstance(self.pet.breed, PetBreed)
        self.assertEquals(str(self.pet.breed), 'Bulldog')

    def test_pet_related_name(self):
        pet_breed = mommy.make(PetBreed)

        self.pet.breed = pet_breed
        self.pet.save()

        self.assertEquals(str(self.pet), str(pet_breed.pets.get()))

    def test_pelage_foreign_attr(self):
        self.pet.pelage.name = 'Short Hair'
        self.pet.pelage.save()

        self.assertIsInstance(self.pet.pelage, PetPelage)
        self.assertEquals(str(self.pet.pelage), 'Short Hair')

    def test_get_absolute_url_method(self):
        self.pet.name = 'Abigodal'
        self.pet.save()

        absolute_url = self.pet.get_absolute_url()

        self.assertEquals(absolute_url, '/pets/abigodal/detail/')

    def test_pet_image_default(self):
        default_img_path = settings.MEDIA_URL + "images/uploads/default.png"
        self.assertEquals(self.pet.image.url, default_img_path)


class PetBreedTestModel(TestCase):

    def setUp(self):
        self.pet_breed = mommy.make(PetBreed)

    def test_string_representation(self):
        self.assertIsInstance(str(self.pet_breed), str)

    def test_pet_breed_slug(self):
        self.pet_breed.name = 'Shih Tzu'
        self.pet_breed.save()

        self.assertEquals(self.pet_breed.slug, 'shih-tzu')


class PetPelageTestModel(TestCase):

    def setUp(self):
        self.pet_pelage = mommy.make(PetPelage)

    def test_string_representation(self):
        self.assertIsInstance(str(self.pet_pelage), str)

    def test_pet_pelage_slug(self):
        self.pet_pelage.name = 'Low Hair'
        self.pet_pelage.save()

        self.assertEquals(self.pet_pelage.slug, 'low-hair')

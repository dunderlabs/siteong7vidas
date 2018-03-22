from django.test import TestCase
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
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

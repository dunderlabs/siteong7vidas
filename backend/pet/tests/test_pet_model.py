from django.test import TestCase
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from backend.pet.models import Pet


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

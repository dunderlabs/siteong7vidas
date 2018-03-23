from django.test import TestCase
from django.urls import reverse_lazy as r
from model_mommy import mommy
from backend.pet.models import Pet


class TestPetDetailUrl(TestCase):

    def setUp(self):
        self.pet = mommy.make(Pet, name='Abigodal')
        self.url = r('pet:detail', kwargs={'slug': self.pet.slug})

    def test_pet_detail_url_name(self):
        url_detail_name = '/pets/abigodal/detail/'
        self.assertEquals(self.url, url_detail_name)

from django.test import TestCase, Client
from django.urls import reverse_lazy as r
from model_mommy import mommy
from backend.pet.models import Pet


class PetTestDetailView(TestCase):

    def setUp(self):
        self.pet = mommy.make(Pet)
        self.url = r('pet:detail', kwargs={'slug': self.pet.slug})
        self.client = Client()

    def test_pet_detail_view_template(self):
        self.response = self.client.get(self.url)

        self.assertTemplateUsed(self.response, 'pet/detail.html')

    def test_pet_detail_view_response(self):
        self.response = self.client.get(self.url)

        self.assertEqual(self.response.status_code, 200)

    def test_pet_detail_view_context(self):
        self.response = self.client.get(self.url)
        pet = self.response.context['pet']

        self.assertEqual(self.pet.name, pet.name)

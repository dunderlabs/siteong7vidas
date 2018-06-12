from django.views.generic.detail import DetailView
from .models import Pet


class PetDetailView(DetailView):

    model = Pet
    template_name = 'pet/detail.html'

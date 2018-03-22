from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Pet


class PetDetailView(DetailView):

    model = Pet

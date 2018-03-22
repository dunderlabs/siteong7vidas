from django.urls import include, path
from .views import PetDetailView

app_name = 'pet'

urlpatterns = [
    path('<slug:slug>/detail/', PetDetailView.as_view() , name='detail'),
]

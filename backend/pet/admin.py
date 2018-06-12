from django.contrib import admin
from .models import Pet, PetBreed, PetPelage


class PetAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PetBreedAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PetPelageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Pet, PetAdmin)
admin.site.register(PetBreed, PetBreedAdmin)
admin.site.register(PetPelage, PetPelageAdmin)

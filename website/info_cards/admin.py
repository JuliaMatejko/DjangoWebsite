from django.contrib import admin
from .models import BasicInfoCard, DetailInfoCard, Species, Size, Sex, Breed

admin.site.register(BasicInfoCard)
admin.site.register(DetailInfoCard)
admin.site.register(Species)
admin.site.register(Size)
admin.site.register(Sex)
admin.site.register(Breed)
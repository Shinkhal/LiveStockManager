from django.contrib import admin
from .models import Owner, Animal, Vaccination

admin.site.register(Owner)
admin.site.register(Animal)
admin.site.register(Vaccination)

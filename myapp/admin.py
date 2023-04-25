from django.contrib import admin
# Register your models here.
from .models import Note, Women

admin.site.register(Note)
admin.site.register(Women)

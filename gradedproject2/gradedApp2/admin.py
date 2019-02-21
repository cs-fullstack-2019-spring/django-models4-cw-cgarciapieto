from django.contrib import admin

# Register your models here.
from .models import Mother
from .models import Child

admin.site.register(Mother)
admin.site.register(Child)
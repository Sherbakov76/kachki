from django.contrib import admin
from django.db import models
from sportsmens.models import Sportsmens, Categories
from django.forms import CheckboxSelectMultiple


class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Sportsmens, ForModelAdmin)
admin.site.register(Categories)


from django.contrib import admin
from django.db import models
from sportsmens.models import Sportsmens, Categories, Rating, SportsmensSportsmensCategory
from django.forms import CheckboxSelectMultiple


class SportsmenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('id', 'name', 'city', 'trener')
    search_fields = ('id', 'name', 'city', 'trener')
    list_filter = ('city', 'category')


admin.site.register(Sportsmens, SportsmenAdmin)
admin.site.register(Categories)
admin.site.register(Rating)
admin.site.register(SportsmensSportsmensCategory)
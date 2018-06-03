from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_list, name="categories_list"),
    path('category/<int:a>', views.category, name="category"),


]
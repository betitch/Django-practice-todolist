from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    path("single/<int:pk>/", views.single, name="single"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("edit/<int:pk>", views.edit, name="edit"),

]
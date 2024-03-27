from django.urls import path
from . import views

app_name = "tasks" #identifier for urls when used in template html file as link
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
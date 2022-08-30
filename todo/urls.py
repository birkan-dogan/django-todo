from django.urls import path
from .views import home, todo_create, todo_update
urlpatterns = [
    path("",home,name="home"),
    path("add/",todo_create,name="add"),  # todo_create view will be worked by "add/" url
    path("update/<int:id>",todo_update, name="update"),
]
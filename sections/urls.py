from django.urls import path
from . import views

urlpatterns = [
    path("sections/", views.view_function, name="view_function"),
]

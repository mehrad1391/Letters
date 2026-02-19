from django.urls import path
from .views import *

urlpatterns = [
    path("letters/", get_letters),
]


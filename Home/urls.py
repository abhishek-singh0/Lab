from django.urls import path
# Added Manually
from . import views

urlpatterns = [
    path('',views.index),
]

from django.urls import path
# Added Manually
from . import views
import Home

urlpatterns = [
    path('',views.index),
 

]

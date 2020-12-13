from django.urls import path
from . import views

urlpatterns = [
    path('',views.muro, name='muro_notas'),  
]

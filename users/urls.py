from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.save_login, name='save_login'),
]

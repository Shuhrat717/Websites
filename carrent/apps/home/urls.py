from django.urls import path
from .views import index, about

app_name = 'home'

urlpatterns = [
    path('', index),
    path('about/', about)


]

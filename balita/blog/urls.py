from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    path('category/<int:pk>/', category),
    path('blog_single/<slug:slug>/', blog_single),
]
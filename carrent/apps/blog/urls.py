from django.urls import path
from .views import blog, blog_single
app_name = 'blog'

urlpatterns = [
     path('', blog),
     path('<int:pk>/', blog_single, name='blog_single'),
]
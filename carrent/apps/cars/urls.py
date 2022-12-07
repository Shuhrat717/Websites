from django.urls import path
from .views import cars, success

app_name = 'cars'

urlpatterns = [
    path('', cars),
    path('<int:pk>/', success),

]

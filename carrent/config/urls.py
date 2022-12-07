from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls',  namespace='home')),
    path('blog/', include('apps.blog.urls',  namespace='blog')),
    path('cars/', include('apps.cars.urls',  namespace='cars')),
    path('contact/', include('apps.contact.urls',  namespace='contact')),
    path('services/', include('apps.services.urls',  namespace='services')),

    path('api/', include('apps.blog.api.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

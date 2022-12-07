from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.articles.urls', namespace='articles')),
    path('comment/', include('apps.comments.urls', namespace='comments')),
    path('about/', include('apps.about.urls', namespace='about')),
    path('contact/', include('apps.contact.urls', namespace='contact')),

    path('api/', include('apps.articles.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


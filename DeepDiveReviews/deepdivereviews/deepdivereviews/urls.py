"""
URL configuration for deepdivereviews project.
"""
from django.contrib import admin
from profiles.urls import profiles_patterns
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('reviews.urls')),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns))
]
""" 
Si el modo DEBUG está activado se activa la opción de servir ficheros media en la URL media, que se 
buscarán en el directorio de MEDIA_ROOT
 """
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
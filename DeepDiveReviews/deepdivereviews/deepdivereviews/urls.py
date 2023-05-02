"""
URL configuration for deepdivereviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from profiles.urls import profiles_patterns
from reviews.urls import reviews_patterns
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    #path('', include('core.urls')),
    path('', include(reviews_patterns)),
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
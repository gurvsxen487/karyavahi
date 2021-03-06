from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
]


if settings.DEBUG:
	urlpatterns+= ( static(settings.STATIC_URL) )

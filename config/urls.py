import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include
from .views import HomeView


urlpatterns = [
    path('nimda/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]

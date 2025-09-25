
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve as static_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)', static_serve,{'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)', static_serve, {'document_root': settings.MEDIA_ROOT}),
]



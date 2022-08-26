from django.contrib import admin
from django.urls import path

from django.conf import settings
from . import views
from django.conf.urls.static      import static

urlpatterns =[
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('', views.inicio),
   # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static('/assets/', document_root=settings.BASE_DIR / 'assets')
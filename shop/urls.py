from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'shop'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
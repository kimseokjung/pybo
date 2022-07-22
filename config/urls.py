
from django.conf.urls.static import static

from config.settings import base
from django.contrib import admin
from django.urls import path, include
from products.views import base_views

urlpatterns = [
    path('', base_views.index, name="index"),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('products/', include('products.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

handler404 = 'common.views.page_not_found_404'

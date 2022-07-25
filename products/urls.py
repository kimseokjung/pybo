from django.urls import path
from .views import base_views, product_views

app_name = 'products'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:product_id>/', base_views.detail, name='detail'),
    path('products/create/', product_views.product_create, name='product_create'),
]
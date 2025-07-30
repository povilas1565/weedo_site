from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_gallery, name='gallery'),
    path('upload/', views.product_upload, name='upload'),
    path('export/', views.export_json, name='export'),
]
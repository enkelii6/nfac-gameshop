from django.urls import path

from . import views

urlpatterns = [
    path('catalog', views.ProductListView.as_view(), name='product-list'),
    path('catalog/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('catalog/<int:pk>/review', views.create_review, name='review-create'),
]

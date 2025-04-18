from django.urls import path

from . import views

urlpatterns = [
    path('basket', views.BasketView.as_view(), name='basket'),
    path('basket/add/<int:product_id>/', views.BasketView.as_view(), name='basket'),
]

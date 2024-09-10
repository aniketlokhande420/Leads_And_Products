from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('leads/create/', LeadCreateAPIView.as_view(), name='lead-create'),
    path('leads/reports/', LeadsBetweenDatesAPIView.as_view(), name='leads-between-dates'),
    path('leads/top-products/', ProductsWithMostLeadsAPIView.as_view(), name='top-10-products'),
    path('leads/bottom-products/', ProductsWithLeastLeadsAPIView.as_view(), name='bottom-10-products'),
    path('leads/products-count/', ProductsInquiredPerLeadAPIView.as_view(), name='products-inquired-count'),
]
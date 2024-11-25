from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter


router= DefaultRouter()
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('products', views.ProductViewSet, basename='products')
router.register('carts', views.CartViewSet, basename='carts')

product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

cart_item_router = NestedDefaultRouter(router, 'carts', lookup='cart')
cart_item_router.register('items', views.CartItemViewSet, basename='cart-item')

urlpatterns = router.urls + product_router.urls + cart_item_router.urls




# urlpatterns = [
#     path('', include(router.urls)),
#
#     path('store/products/', views.ProductList.as_view()),
#
#     path('store/products/<pk>/', views.ProductDetailAPIView.as_view()),
# ]
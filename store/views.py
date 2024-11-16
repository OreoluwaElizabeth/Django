from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (ProductSerializer, CollectionSerializer, CreateProductSerializer,
                          ReviewSerializer, CreateReviewSerializer, CartSerializer, CartItemSerializer, AddToCartSerializer)
from .models import Product, Collection, Review, Cart, CartItem
from .filter import ProductFilter
from .pagination import DefaultPageNumber
from rest_framework.permissions import IsAuthenticated


# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.all()

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ProductSerializer
    #     elif self.request.method == 'POST':
    #         return CreateProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter
    pagination_class = DefaultPageNumber
    permission_classes = [IsAuthenticated]

class CartList(ListCreateAPIView):
    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CartSerializer
        elif self.request.method == 'GET':
            return CartSerializer

# class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = DefaultPageNumber


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewSerializer
        elif self.request.method == 'POST':
            return CreateReviewSerializer
        return ReviewSerializer


# class CollectionListApiView(ListCreateAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
#
# class CollectionDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.prefetch_related('item__product').all()
    serializer_class = CartSerializer



class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddToCartSerializer
        elif self.request.method == 'PATCH':
            return CartUpdateSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}


# @api_view()
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def collection_list(request):
#     collections = Collection.objects.all()
#     serializer = CollectionSerializer(collections, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# def collection_detail(request, pk):
#     collection = get_object_or_404(Collection, pk=pk)
#     serializer = CollectionSerializer(collection)
#     return Response(serializer.data, status=status.HTTP_200_OK)

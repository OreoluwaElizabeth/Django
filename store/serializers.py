from rest_framework import serializers
from decimal import Decimal
from store.models import Collection, Product, Review, Cart, CartItem


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'price_with_discount', 'collection']

    price_with_discount = serializers.SerializerMethodField(method_name='discount_price')

    def discount_price(self, product: Product):
        return product.price * Decimal(0.01)


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'inventory', 'collection']


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'content', 'customer', 'product']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'content']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id']

class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'total_price']


class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer()
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price'
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.price * cart_item.quantity


class AddToCartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except Cart.DoesNotExist:
           self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        return self.instance


    class Meta:
        model = Cart
        fields = ['product-id', 'quantity']


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
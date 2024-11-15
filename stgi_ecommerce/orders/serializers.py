from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_id', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True)
    order_items = OrderItemSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    order_summary = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_id', 'order_date', 'total_amount', 'status', 'order_items', 'order_summary']

    def validate(self, data):

        if 'order_items' in data:
            for item_data in data['order_items']:
                product = Product.objects.get(pk=item_data['product_id'])
                if item_data['quantity'] > product.stock:
                    raise serializers.ValidationError(f"{product.name} is out of stock. Available: {product.stock}")
        return data

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        
        total_amount = 0
        for item_data in order_items_data:
            product = Product.objects.get(pk=item_data['product_id'])
            item_data['price'] = product.price
            OrderItem.objects.create(order=order, product=product, **item_data)
            total_amount += product.price * item_data['quantity']
            product.stock -= item_data['quantity']
            product.save()
        
        order.total_amount = total_amount
        order.save()
        return order

    def get_order_summary(self, obj):
        return [
            {
                "product": item.product.name,
                "quantity": item.quantity,
                "price": item.price,
                "subtotal": item.quantity * item.price
            } 
            for item in obj.order_items.all()
        ]

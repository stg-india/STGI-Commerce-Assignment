from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from django.db.models import Sum
from .filters import OrderFilter

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.select_related('customer').prefetch_related('order_items__product')

    @action(detail=True, methods=['post'])
    def mark_as_shipped(self, request, pk=None):
        order = self.get_object()
        if order.status != Order.PROCESSING:
            return Response(
                {"error": "Only processing orders can be marked as shipped"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = Order.SHIPPED
        order.save()
        return Response({"status": "Order marked as shipped"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def mark_as_delivered(self, request, pk=None):
        order = self.get_object()
        if order.status != Order.SHIPPED:
            return Response(
                {"error": "Only shipped orders can be marked as delivered"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = Order.DELIVERED
        order.save()
        return Response({"status": "Order marked as delivered"}, status=status.HTTP_200_OK)

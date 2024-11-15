import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="order_date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="order_date", lookup_expr='lte')
    status = django_filters.ChoiceFilter(choices=Order.STATUS_CHOICES)
    customer = django_filters.NumberFilter(field_name="customer__id")

    class Meta:
        model = Order
        fields = ['start_date', 'end_date', 'status', 'customer']

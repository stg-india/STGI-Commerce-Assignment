# STGI-Commerce-Assignment
Repository for Assignment Submission


Model Creation:
 
1. Create models for Customer, Product, Order, and OrderItem.
Customer should have fields: name, email, phone, and address.
Product should have fields: name, description, price, and stock.
Order should have fields: customer (ForeignKey to Customer), order_date, total_amount, and status (choices: Pending, Processing, Shipped, Delivered).
OrderItem should have fields: order (ForeignKey to Order), product (ForeignKey to Product), quantity, and price.
 
Serializer Implementation:
 
2. Create serializers for all models. Use nested serializers where appropriate.
Implement custom validation in serializers (e.g., ensure that ordered products are in stock).
Add custom fields in the OrderSerializer such as total_amount (calculated as the sum of all OrderItems) and order_summary (a breakdown of each item ordered).
ViewSet Implementation:
 
3. Create ViewSets for Customer, Product, and Order.
For OrderViewSet, implement a custom action (e.g., @action(detail=True, methods=['POST'])) for marking an order as shipped.
Implement a custom filtering capability in the OrderViewSet to filter orders by customer, status, or date ranges.
Use Django's prefetch_related or select_related to optimize database queries in the OrderViewSet.
Custom Querysets and Filtering:
 
4. Implement custom queryset filtering using django-filters or manual filtering for orders based on:
Date range (e.g., orders between two dates).
Order status (e.g., all "shipped" orders).
Customer-specific queries (e.g., orders made by a specific customer).

STGI E-Commerce Project
This is an assignment project implementing a simple e-commerce application using Django and Django REST framework. It includes models for Customer, Product, Order, and OrderItem, with filters, serializers, and custom view actions for managing and querying data.


# Run Project: 
-> Start the Django development server 
-> python manage.py runserver

# Admin Panel: http://127.0.0.1:8000/admin/

# API Endpoints:
-> Customers: http://127.0.0.1:8000/api/customers/
-> Products: http://127.0.0.1:8000/api/products/
-> Orders: http://127.0.0.1:8000/api/orders/

# API Endpoints
1. Customers Endpoint
-> List Customers: GET /api/customers/
-> Retrieve Customer: GET /api/customers/{id}/
-> Create Customer: POST /api/customers/
-> Update Customer: PUT /api/customers/{id}/
-> Delete Customer: DELETE /api/customers/{id}/
2. Products Endpoint
-> List Products: GET /api/products/
-> Retrieve Product: GET /api/products/{id}/
-> Create Product: POST /api/products/
-> Update Product: PUT /api/products/{id}/
-> Delete Product: DELETE /api/products/{id}/
3. Orders Endpoint
-> List Orders: GET /api/orders/
-> Retrieve Order: GET /api/orders/{id}/
-> Create Order: POST /api/orders/
-> Update Order: PUT /api/orders/{id}/
-> Delete Order: DELETE /api/orders/{id}/
-> Mark as Shipped: POST /api/orders/{id}/mark_as_shipped/
-> Mark as Delivered: POST /api/orders/{id}/mark_as_delivered/
-> Filter Orders: You can filter orders by customer, status, start_date, and end_date.

4. Order Items
-> Order items are automatically handled when creating or updating an order. To view or manage specific order items, you will need to use the Django Admin panel.

# You can create and manage OrderItem entries through the admin interface, as they are tied to Order instances.

Admin Credentials:
Username: admin
Password: admin

# Filtering Orders:

You can filter orders by customer, status, and date ranges directly through the GET /api/orders/ endpoint by passing query parameters.

from django.urls import path
from ecommerce.views import (
    
    ecommerce_product,
    ecommerce_product_details,
    ecommerce_orders,
    ecommerce_customers,
    ecommerce_cart,
    ecommerce_checkout,
    ecommerce_shop,
    ecommerce_add_product,
)

app_name = 'ecommerce'

urlpatterns = [
    
    path('product',view=ecommerce_product,name="product"),
    path('product_detail',view=ecommerce_product_details,name="product_detail"),
    path('orders',view=ecommerce_orders,name="orders"),
    path('customers',view=ecommerce_customers,name="customers"),
    path('cart',view=ecommerce_cart,name="cart"),
    path('checkout',view=ecommerce_checkout,name="checkout"),
    path('shop',view=ecommerce_shop,name="shop"),
    path('add_product',view=ecommerce_add_product,name="add_product"),
]

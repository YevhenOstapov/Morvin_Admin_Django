from django.shortcuts import render
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class EcommerceView(LoginRequiredMixin, View):
    pass

ecommerce_product = EcommerceView.as_view( _name = "ecommerce/ecommerce-products.html")
ecommerce_product_details = EcommerceView.as_view( _name = "ecommerce/ecommerce-product-detail.html")
ecommerce_orders = EcommerceView.as_view( _name = "ecommerce/ecommerce-orders.html")
ecommerce_customers = EcommerceView.as_view( _name = "ecommerce/ecommerce-customers.html")
ecommerce_cart = EcommerceView.as_view( _name = "ecommerce/ecommerce-cart.html")
ecommerce_checkout = EcommerceView.as_view( _name = "ecommerce/ecommerce-checkout.html")
ecommerce_shop = EcommerceView.as_view( _name = "ecommerce/ecommerce-shops.html")
ecommerce_add_product = EcommerceView.as_view( _name = "ecommerce/ecommerce-add-product.html")

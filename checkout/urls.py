from django.urls import path
from checkout.views import checkout_view, webhook_view, success_view, fail_view

urlpatterns = [
    path('', checkout_view, name="checkout"),
    path('payment-success/', success_view, name="success_view"),
    path('payment-failed/', fail_view, name="fail_view"),
    path('webhook/', webhook_view, name="webhook_view"),
]

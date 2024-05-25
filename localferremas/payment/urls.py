# En tu archivo urls.py

from django.urls import path
from .views import payment, verify_transaction

urlpatterns = [
    path('payment/<int:pedido_id>/', payment, name='payment'),
    path('verify_transaction/', verify_transaction, name='verify_transaction'),
]

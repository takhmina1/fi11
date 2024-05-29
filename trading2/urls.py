from django.urls import path
from .views import (
    TransactionListCreateAPIView,
    TransactionRetrieveUpdateDestroyAPIView,
    CurrencyConversionAPIView,
    SupportedCurrenciesAPIView,
)

urlpatterns = [
    path('/transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction-retrieve-update-destroy'),
    path('currency/convert/', CurrencyConversionAPIView.as_view(), name='currency-conversion'),
    path('currency/supported/', SupportedCurrenciesAPIView.as_view(), name='supported-currencies'),
]

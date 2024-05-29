from django.urls import path
from .views import *

urlpatterns = [
    path('crypto_wallet/', CryptoWalletAPIView.as_view(), name='crypto_wallet'),
    path('fiat_wallet/', FiatWalletAPIView.as_view(), name='fiat_wallet'),
    path('exchange_pair/', ExchangePairAPIView.as_view(), name='exchange_pair'),
    path('transaction/', TransactionAPIView.as_view(), name='transaction'),
]

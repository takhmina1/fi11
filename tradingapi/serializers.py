from rest_framework import serializers
from .models import Currency, CryptoCurrency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['currency_code', 'currency_name', 'exchange_rate', 'last_updated']

class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['currency_code', 'currency_name', 'exchange_rate', 'last_updated']

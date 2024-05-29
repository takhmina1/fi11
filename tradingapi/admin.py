from django.contrib import admin
from .models import Currency, CryptoCurrency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_code', 'currency_name', 'exchange_rate', 'last_updated')
    search_fields = ('currency_code', 'currency_name')
    list_filter = ('currency_code',)
    ordering = ('currency_code',)

@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_code', 'currency_name', 'exchange_rate', 'last_updated')
    search_fields = ('currency_code', 'currency_name')
    list_filter = ('currency_code',)
    ordering = ('currency_code',)

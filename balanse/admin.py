from django.contrib import admin
from .models import CryptoWallet, FiatWallet, CryptoCurrency, ExchangePair, Transaction

@admin.register(CryptoWallet)
class CryptoWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'balance')
    search_fields = ('user__username', 'currency__name')

@admin.register(FiatWallet)
class FiatWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'balance')
    search_fields = ('user__username', 'currency')

@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'current_price')
    search_fields = ('name', 'symbol')

@admin.register(ExchangePair)
class ExchangePairAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'target_currency', 'commission_rate')
    search_fields = ('base_currency__name', 'target_currency__name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'exchange_pair', 'amount_base', 'amount_target', 'commission_amount', 'timestamp', 'status')
    list_filter = ('status', 'timestamp')
    search_fields = ('user__username', 'exchange_pair__base_currency__name', 'exchange_pair__target_currency__name')

from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'amount', 'currency_type', 'timestamp')
    list_filter = ('transaction_type', 'currency_type')
    search_fields = ('user__username', 'amount', 'currency_type')
    readonly_fields = ('timestamp',)












# from django.contrib import admin
# from .models import CurrencyConverter, Transaction
# from .currency_converter import conversion_rates

# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('user', 'transaction_type', 'amount', 'currency_type', 'timestamp')
#     list_filter = ('transaction_type', 'timestamp')
#     search_fields = ['user__username', 'transaction_type', 'currency_type']
#     readonly_fields = ('timestamp',)

# admin.site.register(Transaction, TransactionAdmin)


# class ConversionRatesAdmin(admin.ModelAdmin):
#     list_display = ('from_currency', 'to_currency', 'conversion_rate')

#     def save_model(self, request, obj, form, change):
#         # При сохранении модели обновляем коэффициент конверсии с использованием conversion_rates
#         from_currency = obj.from_currency
#         to_currency = obj.to_currency
#         conversion_rate = obj.conversion_rate

#         # Сохраняем коэффициент конверсии в базе данных
#         obj.save()

#         # Обновляем коэффициент конверсии в памяти (если необходимо)
#         conversion_rates.update_conversion_rate(from_currency, to_currency, conversion_rate)

# admin.site.register(CurrencyConverter, ConversionRatesAdmin())

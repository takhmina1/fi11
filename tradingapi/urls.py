# # # # from django.urls import path, include
# # # # from rest_framework.routers import DefaultRouter
# # # # from .views import CurrencyExchangeViewSet

# # # # router = DefaultRouter()
# # # # router.register(r'currency-exchange', CurrencyExchangeViewSet, basename='currency-exchange')

# # # # urlpatterns = [
# # # #     path('', include(router.urls)),
# # # #     path('currency-exchange/fiat/', CurrencyExchangeViewSet.as_view({'get': 'get_fiat_currency_exchange_rates'}), name='fiat-currency-exchange-rates'),
# # # #     path('currency-exchange/crypto/', CurrencyExchangeViewSet.as_view({'get': 'get_crypto_currency_exchange_rates'}), name='crypto-currency-exchange-rates'),
# # # # ]




# # # from django.urls import path, include
# # # from rest_framework.routers import DefaultRouter
# # # from .views import CurrencyExchangeViewSet

# # # # Создаем роутер и регистрируем наш ViewSet
# # # router = DefaultRouter()
# # # router.register(r'currency-exchange', CurrencyExchangeViewSet, basename='currency-exchange')

# # # # # URL-ы для приложения
# # # urlpatterns = [
# # #     path('', include(router.urls)),
# # # ]

# # # # Дополнительные пути, если нужны прямые маршруты
# # # urlpatterns += [
# # #     path('currency-exchange/fiat/', CurrencyExchangeViewSet.as_view({'get': 'fiat'}), name='fiat-currency-exchange-rates'),
# # #     path('currency-exchange/crypto/', CurrencyExchangeViewSet.as_view({'get': 'crypto'}), name='crypto-currency-exchange-rates'),
# # # ]



# # # # from django.urls import path, include
# # # # from rest_framework.routers import DefaultRouter
# # # # from .views import CurrencyExchangeViewSet

# # # # router = DefaultRouter()
# # # # router.register(r'currency-exchange', CurrencyExchangeViewSet, basename='currency-exchange')

# # # # urlpatterns = [
# # # #     path('', include(router.urls)),
# # # # ]





# # from django.urls import path
# # from rest_framework.routers import DefaultRouter
# # from .views import CurrencyExchangeViewSet

# # router = DefaultRouter()
# # router.register(r'currency', CurrencyExchangeViewSet, basename='currency-exchange')

# # urlpatterns = router.urls



# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import CurrencyExchangeViewSet

# router = DefaultRouter()
# router.register(r'currency', CurrencyExchangeViewSet, basename='currency-exchange')

# urlpatterns = [
#     path('currency/fiat/', CurrencyExchangeViewSet.as_view({'get': 'fiat'}), name='fiat'),
#     path('currency/crypto/', CurrencyExchangeViewSet.as_view({'get': 'crypto'}), name='crypto'),
# ]

# urlpatterns += router.urls



# from django.urls import path
# from .views import CurrencyExchangeViewSet

# urlpatterns = [
#     path('api3/', CurrencyExchangeViewSet.as_view(), name='currency_exchange_root'),
# ]


# from django.urls import path
# from .views import update_currency_data_view

# urlpatterns = [
#     path('update_currency_data/', update_currency_data_view, name='update_currency_data'),
#     # Дополнительные маршруты, если это необходимо
# ]

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyExchangeViewSet

router = DefaultRouter()
router.register(r'currency-exchange', CurrencyExchangeViewSet, basename='currency-exchange')

urlpatterns = [
    path('', include(router.urls)),
]

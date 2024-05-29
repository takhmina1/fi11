# # # # # views.py
# # # # from rest_framework import viewsets
# # # # from rest_framework.response import Response
# # # # from rest_framework.decorators import action
# # # # from rest_framework import status
# # # # from .serializers import CurrencySerializer
# # # # from .services import fetch_data_from_fx_kg_api, fetch_data_from_coingecko_api

# # # # class CurrencyExchangeViewSet(viewsets.ViewSet):
# # # #     @action(detail=False, methods=['get'])
# # # #     def get_fiat_currency_exchange_rates(self, request):
# # # #         """
# # # #         Получает данные о курсах фиатных валют из внешнего API и возвращает их в формате JSON.
# # # #         """
# # # #         fiat_currencies_data = asyncio.run(fetch_data_from_fx_kg_api())
# # # #         return Response(fiat_currencies_data, status=status.HTTP_200_OK)

# # # #     @action(detail=False, methods=['get'])
# # # #     def get_crypto_currency_exchange_rates(self, request):
# # # #         """
# # # #         Получает данные о курсах криптовалют из внешнего API и возвращает их в формате JSON.
# # # #         """
# # # #         crypto_currencies_data = asyncio.run(fetch_data_from_coingecko_api())
# # # #         return Response(crypto_currencies_data, status=status.HTTP_200_OK)








# # # # views.py
# # # from rest_framework import viewsets
# # # from rest_framework.response import Response
# # # from rest_framework.decorators import action
# # # from rest_framework import status
# # # from .services import fetch_data_from_fx_kg_api, fetch_data_from_coingecko_api
# # # import asyncio

# # # class CurrencyExchangeViewSet(viewsets.ViewSet):
# # #     @action(detail=False, methods=['get'])
# # #     def fiat(self, request):
# # #         """
# # #         Получает данные о курсах фиатных валют из внешнего API и возвращает их в формате JSON.
# # #         """
# # #         fiat_currencies_data = asyncio.run(fetch_data_from_fx_kg_api())

# # #         if "error" in fiat_currencies_data:
# # #             return Response({"error": fiat_currencies_data["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # #         return Response(fiat_currencies_data, status=status.HTTP_200_OK)

# # #     @action(detail=False, methods=['get'])
# # #     def crypto(self, request):
# # #         """
# # #         Получает данные о курсах криптовалют из внешнего API и возвращает их в формате JSON.
# # #         """
# # #         crypto_currencies_data = asyncio.run(fetch_data_from_coingecko_api())

# # #         if "error" in crypto_currencies_data:
# # #             return Response({"error": crypto_currencies_data["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # #         return Response(crypto_currencies_data, status=status.HTTP_200_OK)




# # # # views.py
# # # from rest_framework import viewsets
# # # from rest_framework.response import Response
# # # from rest_framework.decorators import action
# # # from rest_framework import status
# # # from .services import fetch_data_from_fx_kg_api, fetch_data_from_coingecko_api
# # # import asyncio

# # # class CurrencyExchangeViewSet(viewsets.ViewSet):
# # #     @action(detail=False, methods=['get'])
# # #     def fiat(self, request):
# # #         """
# # #         Получает данные о курсах фиатных валют из внешнего API и возвращает их в формате JSON.
# # #         """
# # #         try:
# # #             fiat_currencies_data = asyncio.run(fetch_data_from_fx_kg_api())
# # #             return Response(fiat_currencies_data, status=status.HTTP_200_OK)
# # #         except Exception as e:
# # #             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# # #         return request

# # #     @action(detail=False, methods=['get'])
# # #     def crypto(self, request):
# # #         """
# # #         Получает данные о курсах криптовалют из внешнего API и возвращает их в формате JSON.
# # #         """
# # #         try:
# # #             crypto_currencies_data = asyncio.run(fetch_data_from_coingecko_api())
# # #             return Response(crypto_currencies_data, status=status.HTTP_200_OK)
# # #         except Exception as e:
# # #             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# # #         return request




# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework import status
# from .services import fetch_data_from_fx_kg_api, fetch_data_from_coingecko_api
# import asyncio

# class CurrencyExchangeViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['get'])
#     def fiat(self, request):
#         """
#         Получает данные о курсах фиатных валют из внешнего API и возвращает их в формате JSON.
#         """
#         try:
#             fiat_currencies_data = asyncio.run(fetch_data_from_fx_kg_api())
#             return Response(fiat_currencies_data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         return request
# #     @action(detail=False, methods=['get'])
# #     def crypto(self, request):
# #         """
# #         Получает данные о курсах криптовалют из внешнего API и возвращает их в формате JSON.
# #         """
# #         try:
# #             crypto_currencies_data = asyncio.run(fetch_data_from_coingecko_api())
# #             return Response(crypto_currencies_data, status=status.HTTP_200_OK)
# #         except Exception as e:
# #             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .services import fetch_data_from_fx_kg_api

# # class CurrencyExchangeRootView(APIView):
# #     def get(self, request):
# #         try:
# #             fiat_currencies_data = asyncio.run(fetch_data_from_fx_kg_api())
# #             return Response(fiat_currencies_data, status=status.HTTP_200_OK)
# #         except Exception as e:
# #             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# #         return request





# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
# from .services import fetch_data_from_fx_kg_api, fetch_data_from_coingecko_api

# @require_GET
# async def update_currency_data_view(request):
#     fiat_data = await fetch_data_from_fx_kg_api()
#     crypto_data = await fetch_data_from_coingecko_api()

#     # Обработка полученных данных и сохранение их в базу данных
#     if "error" not in fiat_data:
#         await save_currency_data_to_database(fiat_data)
    
#     if "error" not in crypto_data:
#         await save_currency_data_to_database(crypto_data, is_crypto=True)

#     return JsonResponse({"message": "Currency data updated successfully"})

# # Дополнительные представления для получения данных о валютах и криптовалютах, если это необходимо







# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from .models import Currency, CryptoCurrency
# import asyncio
# import httpx

# @require_http_methods(["GET"])
# async def update_currency_data_view(request):
#     fiat_data = await fetch_data_from_fx_kg_api()
#     if "error" not in fiat_data:
#         formatted_fiat_data = format_currency_data(fiat_data)
#         await save_currency_data_to_database(formatted_fiat_data)

#     crypto_data = await check_coingecko_api()
#     if "error" not in crypto_data:
#         await save_currency_data_to_database(crypto_data, is_crypto=True)

#     return JsonResponse({"message": "Currency data updated successfully."})

# async def check_coingecko_api():
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         'ids': 'bitcoin,ethereum',  # Добавляем ethereum в запрос, если вам нужны данные для обеих криптовалют
#         'vs_currencies': 'usd'
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, params=params)
#         response.raise_for_status()  # Проверка на наличие ошибок
#         data = response.json()

#         formatted_data = []
#         for currency_code, currency_info in data.items():
#             formatted_data.append({
#                 'currency_code': currency_code,
#                 'currency_name': currency_info['currency_code'].capitalize(),  # Первая буква в верхнем регистре
#                 'exchange_rate': currency_info['usd']  # Обменный курс в USD
#             })

#         return formatted_data

# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .services import fetch_data_from_fx_kg_api, fetch_data_from_coingecko_api
import asyncio

class CurrencyExchangeViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def fiat(self, request):
        """
        Получает данные о курсах фиатных валют из внешнего API и возвращает их в формате JSON.
        """
        try:
            fiat_currencies_data = asyncio.run(fetch_data_from_fx_kg_api())
            return Response(fiat_currencies_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def crypto(self, request):
        """
        Получает данные о курсах криптовалют из внешнего API и возвращает их в формате JSON.
        """
        try:
            crypto_currencies_data = asyncio.run(fetch_data_from_coingecko_api())
            return Response(crypto_currencies_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

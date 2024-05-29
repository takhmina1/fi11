# import httpx
# import asyncio
# from .models import Currency, CryptoCurrency



# async def fetch_data_from_fx_kg_api():
#     url = "https://data.fx.kg/api/v1/currencies"
#     headers = {
#         'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'
#     }

#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers)
#             response.raise_for_status()  # Проверка на наличие ошибок
#             data = response.json()
#             return data
#         except (httpx.HTTPStatusError, httpx.RequestError) as e:
#             return {"error": str(e)}



# async def fetch_data_from_coingecko_api():
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         'ids': 'bitcoin',
#         'vs_currencies': 'usd'
#     }

#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, params=params)
#             response.raise_for_status()  # Проверка на наличие ошибок
#             data = response.json()
#             return data
#         except (httpx.HTTPStatusError, httpx.RequestError) as e:
#             return {"error": str(e)}



# async def save_currency_data_to_database(data, is_crypto=False):
#     currency_model = CryptoCurrency if is_crypto else Currency
    
#     for currency_data in data:
#         currency_code = currency_data.get('currency_code')
#         currency_name = currency_data.get('currency_name')
#         exchange_rate = currency_data.get('exchange_rate')

#         currency, created = currency_model.objects.get_or_create(currency_code=currency_code)
#         if not created:
#             currency.currency_name = currency_name
#             currency.exchange_rate = exchange_rate
#             currency.save()

#     # # Дополнительная логика обработки данных
#     # # Например, удаление устаревших данных
#     # # Удаляем валюты, которые не были обновлены в текущем запросе
#     # outdated_currencies = currency_model.objects.exclude(currency_code__in=[currency_data['currency_code'] for currency_data in data])
#     # outdated_currencies.delete()


# async def update_currency_data():
#     while True:
#         # Fetch data from fx.kg API
#         fx_kg_data = await fetch_data_from_fx_kg_api()
#         if "error" not in fx_kg_data:
#             await save_currency_data_to_database(fx_kg_data)

#         # Fetch data from Coingecko API
#         coingecko_data = await fetch_data_from_coingecko_api()
#         if "error" not in coingecko_data:
#             await save_currency_data_to_database(coingecko_data, is_crypto=True)

#         await asyncio.sleep(45)

'''



import httpx
import asyncio
from .models import Currency, CryptoCurrency

async def fetch_data_from_fx_kg_api():
    url = "https://data.fx.kg/api/v1/currencies"
    headers = {
        'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # Проверка на наличие ошибок
            data = response.json()
            return data
        except (httpx.HTTPStatusError, httpx.RequestError) as e:
            return {"error": str(e)}

async def fetch_data_from_coingecko_api():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()  # Проверка на наличие ошибок
            data = response.json()
            # Преобразуем данные в формат, совместимый с нашей базой данных
            formatted_data = []
            for currency_code, exchange_data in data.items():
                formatted_data.append({
                    'currency_code': currency_code,
                    'currency_name': currency_code.upper(),
                    'exchange_rate': exchange_data['usd']
                })
            return formatted_data
        except (httpx.HTTPStatusError, httpx.RequestError) as e:
            return {"error": str(e)}

async def save_currency_data_to_database(data, is_crypto=False):
    currency_model = CryptoCurrency if is_crypto else Currency
    
    for currency_data in data:
        currency_code = currency_data.get('currency_code')
        currency_name = currency_data.get('currency_name')
        exchange_rate = currency_data.get('exchange_rate')

        currency, created = currency_model.objects.get_or_create(currency_code=currency_code)
        currency.currency_name = currency_name
        currency.exchange_rate = exchange_rate
        currency.save()

    # Дополнительная логика обработки данных
    outdated_currencies = currency_model.objects.exclude(currency_code__in=[currency_data['currency_code'] for currency_data in data])
    outdated_currencies.delete()

async def update_currency_data():
    while True:
        fiat_data = await fetch_data_from_fx_kg_api()
        if "error" not in fiat_data:
            await save_currency_data_to_database(fiat_data)
        
        crypto_data = await fetch_data_from_coingecko_api()
        if "error" not in crypto_data:
            await save_currency_data_to_database(crypto_data, is_crypto=True)
        
        await asyncio.sleep(45)  # Подождать 45 секунд перед следующим обновлением данных

'''



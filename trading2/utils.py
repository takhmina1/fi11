# class CurrencyConverter:
#     @staticmethod
#     def update_conversion_rate(from_currency, to_currency, conversion_rate):
#         """
#         Обновляет коэффициент конверсии между двумя валютами.

#         :param from_currency: Исходная валюта.
#         :param to_currency: Целевая валюта.
#         :param conversion_rate: Новый коэффициент конверсии.
#         """
#         # Здесь можно добавить логику сохранения в базе данных или файл
#         # Например, сохранение в базе данных:
#         ConversionRate.objects.update_or_create(
#             from_currency=from_currency,
#             to_currency=to_currency,
#             defaults={'conversion_rate': conversion_rate}
#         )

#         # Или сохранение в файл, например, в формате JSON:
#         with open('conversion_rates.json', 'w') as file:
#             data = {'from_currency': from_currency, 'to_currency': to_currency, 'conversion_rate': conversion_rate}
#             json.dump(data, file)


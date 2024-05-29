from rest_framework import serializers
from .models import Transaction
from .currency_converter import conversion_rates

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CurrencyConverterSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    from_currency = serializers.CharField(max_length=50)
    to_currency = serializers.CharField(max_length=50)

    def validate(self, data):
        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')

        if from_currency == to_currency:
            raise serializers.ValidationError("Cannot convert between the same currencies.")

        if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
            raise serializers.ValidationError("Conversion between these currencies is not supported.")

        return data

    def convert_currency(self):
        amount = self.validated_data['amount']
        from_currency = self.validated_data['from_currency']
        to_currency = self.validated_data['to_currency']

        conversion_rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate

        return converted_amount

class UserTransactionsSerializer(serializers.Serializer):
    transactions = TransactionSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    average_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_transaction = TransactionSerializer()
    min_transaction = TransactionSerializer()

class TransactionTrendSerializer(serializers.Serializer):
    trend = serializers.CharField(max_length=50)

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



class CurrencyConverterSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    from_currency = serializers.CharField(max_length=50)
    to_currency = serializers.CharField(max_length=50)

    def validate(self, data):
        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')

        if from_currency == to_currency:
            raise serializers.ValidationError("Cannot convert between the same currencies.")

        if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
            raise serializers.ValidationError("Conversion between these currencies is not supported.")

        return data

    def convert_currency(self):
        amount = self.validated_data['amount']
        from_currency = self.validated_data['from_currency']
        to_currency = self.validated_data['to_currency']

        conversion_rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate

        return converted_amount

    def get_supported_currencies(self):
        try:
            # Пытаемся получить список поддерживаемых валют из словаря conversion_rates
            supported_currencies = list(conversion_rates.keys())
            return supported_currencies
        except Exception as e:
            # Обрабатываем исключение в случае ошибки
            # Например, можем залогировать ошибку для последующего анализа
            # Здесь можно настроить обработку ошибки в соответствии с требованиями приложения
            print(f"Произошла ошибка при получении списка поддерживаемых валют: {e}")
            return []  # Возвращаем пустой список в случае ошибки

        

    def get_conversion_rate(self):
        from_currency = self.validated_data['from_currency']
        to_currency = self.validated_data['to_currency']

        if from_currency == to_currency:
            return 1.0

        if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
            return None

        return conversion_rates[from_currency][to_currency]


    
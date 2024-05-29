from rest_framework import serializers
from .models import CryptoWallet, FiatWallet, CryptoCurrency, ExchangePair, Transaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = '__all__'

class CryptoWalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CryptoWallet
        fields = ['user', 'currency', 'balance']

    def update_balance(self, instance, validated_data):
        """
        Метод для обновления баланса криптовалютного кошелька.
        """
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

class FiatWalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FiatWallet
        fields = ['user', 'currency', 'balance']

    def update_balance(self, instance, validated_data):
        """
        Метод для обновления баланса фиатного кошелька.
        """
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

class ExchangePairSerializer(serializers.ModelSerializer):
    base_currency = CryptoCurrencySerializer()
    target_currency = CryptoCurrencySerializer()

    class Meta:
        model = ExchangePair
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    exchange_pair = ExchangePairSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'


























# from rest_framework import serializers
# from .models import CryptoWallet, FiatWallet, CryptoCurrency, ExchangePair, Transaction
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']    

# class CryptoCurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CryptoCurrency
#         fields = '__all__'

# class CryptoWalletSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = CryptoWallet
#         fields = ['user', 'currency', 'balance']

#     def update_balance(self, instance, validated_data):
#         """
#         Метод для обновления баланса криптовалютного кошелька.
#         """
#         instance.balance = validated_data.get('balance', instance.balance)
#         instance.save()
#         return instance

# class FiatWalletSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = FiatWallet
#         fields = ['user', 'currency', 'balance']

#     def update_balance(self, instance, validated_data):
#         """
#         Метод для обновления баланса фиатного кошелька.
#         """
#         instance.balance = validated_data.get('balance', instance.balance)
#         instance.save()
#         return instance

# class ExchangePairSerializer(serializers.ModelSerializer):
#     base_currency = CryptoCurrencySerializer()
#     target_currency = CryptoCurrencySerializer()

#     class Meta:
#         model = ExchangePair
#         fields = '__all__'

# class TransactionSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     exchange_pair = ExchangePairSerializer()

#     class Meta:
#         model = Transaction
#         fields = '__all__'

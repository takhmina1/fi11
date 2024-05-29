from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CryptoWallet, FiatWallet, ExchangePair, Transaction
from .serializers import CryptoCurrencySerializer, FiatWalletSerializer, ExchangePairSerializer, TransactionSerializer
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class CryptoWalletAPIView(APIView):
    @swagger_auto_schema(operation_description="Создание криптовалютного кошелька пользователя")
    def post(self, request, *args, **kwargs):
        """
        Метод POST для создания криптовалютного кошелька пользователя.
        """
        # Получаем user_id из параметров запроса
        user_id = kwargs.get('user_id')

        # Создаем экземпляр сериализатора и передаем ему данные из запроса
        serializer = CryptoCurrencySerializer(data=request.data)
        
        # Проверяем валидность данных
        if serializer.is_valid():
            # Если данные валидны, сохраняем их, учитывая переданный идентификатор пользователя
            serializer.save(user_id=user_id)
            # Возвращаем успешный ответ с данными созданного объекта и статусом HTTP 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Если данные невалидны, возвращаем ответ с ошибками валидации и статусом HTTP 400 Bad Request
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(operation_description="Получение информации о криптовалютном кошельке пользователя")
    def get(self, request):
        """
        Метод GET для получения информации о криптовалютном кошельке пользователя.
        """
        user = request.user  # Предполагается, что запрос приходит от аутентифицированного пользователя
        try:
            crypto_wallet = CryptoWallet.objects.get(user=user)
            serializer = CryptoCurrencySerializer(crypto_wallet)
            return Response(serializer.data)
        except CryptoWallet.DoesNotExist:
            return Response({"detail": "Криптовалютный кошелек пользователя не найден"}, status=status.HTTP_404_NOT_FOUND)


class FiatWalletAPIView(APIView):
    @swagger_auto_schema(operation_description="Метод POST для создания фиатного кошелька")
    def post(self, request):
        """
        Создание фиатного кошелька пользователя.
        """
        serializer = FiatWalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(operation_description="Метод GET для получения информации о фиатном кошельке")
    def get(self, request):
        """
        Получение информации о фиатном кошельке пользователя.
        """
        user = request.user  # Получение пользователя из запроса
        fiat_wallet = FiatWallet.objects.get(user=user)
        serializer = FiatWalletSerializer(fiat_wallet)
        return Response(serializer.data)


class ExchangePairAPIView(APIView):
    @swagger_auto_schema(operation_description="Описание метода POST для создания пары обмена криптовалюты")
    def post(self, request):
        """
        Создание пары обмена криптовалюты.
        """
        serializer = ExchangePairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Описание метода GET для получения информации о паре обмена криптовалюты")
    def get(self, request):
        """
        Получение информации о паре обмена криптовалюты.
        """
        exchange_pairs = ExchangePair.objects.all()
        serializer = ExchangePairSerializer(exchange_pairs, many=True)
        return Response(serializer.data)


class TransactionAPIView(APIView):
    @swagger_auto_schema(operation_description="Описание метода POST для создания транзакции")
    def post(self, request):
        """
        Создание транзакции.
        """
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(operation_description="Описание метода GET для получения информации о транзакции")
    def get(self, request):
            """
            Получение информации о транзакции.
            """
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data)
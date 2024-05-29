from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Transaction
from .serializers import TransactionSerializer
from .currency_converter import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TransactionListCreateAPIView(APIView):
    """
    Представление для списка и создания транзакций.
    """
    @swagger_auto_schema(responses={200: TransactionSerializer(many=True)})
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TransactionSerializer, responses={201: TransactionSerializer()})
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionRetrieveUpdateDestroyAPIView(APIView):
    """
    Представление для получения, обновления и удаления транзакции.
    """
    @swagger_auto_schema(responses={200: TransactionSerializer()})
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TransactionSerializer, responses={200: TransactionSerializer()})
    def put(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: "No Content"})
    def delete(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrencyConversionAPIView(APIView):
    """
    Представление для конвертации валюты.
    """
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER),
            'from_currency': openapi.Schema(type=openapi.TYPE_STRING),
            'to_currency': openapi.Schema(type=openapi.TYPE_STRING)
        }
    ), responses={200: openapi.Schema(type=openapi.TYPE_OBJECT, properties={'converted_amount': openapi.Schema(type=openapi.TYPE_NUMBER)})})
    def post(self, request):
        amount = request.data.get('amount')
        from_currency = request.data.get('from_currency')
        to_currency = request.data.get('to_currency')

        if not all([amount, from_currency, to_currency]):
            return Response({'error': 'Необходимо указать amount, from_currency и to_currency'}, status=status.HTTP_400_BAD_REQUEST)

        converted_amount, error = CurrencyConverter.convert_currency(float(amount), from_currency, to_currency)

        if error:
            return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'converted_amount': converted_amount})


class SupportedCurrenciesAPIView(APIView):
    """
    Представление для получения списка поддерживаемых валют.
    """
    @swagger_auto_schema(responses={200: openapi.Schema(type=openapi.TYPE_OBJECT, properties={'supported_currencies': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))})})
    def get(self, request):
        supported_currencies = CurrencyConverter.get_supported_currencies()
        return Response({'supported_currencies': supported_currencies})

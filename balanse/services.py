from .models import CryptoWallet, FiatWallet
from .models import ExchangePair, Transaction
from .models import CryptoWallet, FiatWallet, ExchangePair, Transaction

def update_crypto_wallet_balance(user, currency, balance):
    """
    Функция для обновления баланса криптовалютного кошелька пользователя.
    """
    try:
        crypto_wallet = CryptoWallet.objects.get(user=user, currency=currency)
        crypto_wallet.balance = balance
        crypto_wallet.save()
        return crypto_wallet
    except CryptoWallet.DoesNotExist:
        # Если кошелек не найден, можно создать новый
        crypto_wallet = CryptoWallet.objects.create(user=user, currency=currency, balance=balance)
        return crypto_wallet

def update_fiat_wallet_balance(user, currency, balance):
    """
    Функция для обновления баланса фиатного кошелька пользователя.
    """
    try:
        fiat_wallet = FiatWallet.objects.get(user=user, currency=currency)
        fiat_wallet.balance = balance
        fiat_wallet.save()
        return fiat_wallet
    except FiatWallet.DoesNotExist:
        # Если кошелек не найден, можно создать новый
        fiat_wallet = FiatWallet.objects.create(user=user, currency=currency, balance=balance)
        return fiat_wallet


def create_transaction(user, exchange_pair, amount_base):
    """
    Функция для создания транзакции.
    """
    target_amount = amount_base * exchange_pair.target_currency.current_price
    commission_amount = amount_base * exchange_pair.commission_rate / 100

    transaction = Transaction.objects.create(
        user=user,
        exchange_pair=exchange_pair,
        amount_base=amount_base,
        amount_target=target_amount,
        commission_amount=commission_amount,
        status='pending'
    )

    return transaction

def update_transaction_status(transaction, new_status):
    """
    Функция для обновления статуса транзакции.
    """
    transaction.status = new_status
    transaction.save()
    return transaction



def update_crypto_wallet_balance(user, currency, balance):
    try:
        # Пытаемся найти криптовалютный кошелек пользователя для указанной валюты
        crypto_wallet = CryptoWallet.objects.get(user=user, currency=currency)
        crypto_wallet.balance = balance  # Устанавливаем новый баланс
        crypto_wallet.save()  # Сохраняем изменения
        return crypto_wallet  # Возвращаем обновленный объект криптовалютного кошелька
    except CryptoWallet.DoesNotExist:
        # Если криптовалютного кошелька пользователя для указанной валюты не существует, создаем новый
        crypto_wallet = CryptoWallet.objects.create(user=user, currency=currency, balance=balance)
        return crypto_wallet



def update_fiat_wallet_balance(user, currency, balance):
    try:
        # Пытаемся найти фиатный кошелек пользователя для указанной валюты
        fiat_wallet = FiatWallet.objects.get(user=user, currency=currency)
        fiat_wallet.balance = balance  # Устанавливаем новый баланс
        fiat_wallet.save()  # Сохраняем изменения
        return fiat_wallet  # Возвращаем обновленный объект фиатного кошелька
    except FiatWallet.DoesNotExist:
        # Если фиатного кошелька пользователя для указанной валюты не существует, создаем новый
        fiat_wallet = FiatWallet.objects.create(user=user, currency=currency, balance=balance)
        return fiat_wallet




def create_transaction(user, exchange_pair, amount_base):
    # Создаем новую транзакцию
    transaction = Transaction.objects.create(
        user=user,
        exchange_pair=exchange_pair,
        amount_base=amount_base,
        amount_target=amount_base * exchange_pair.target_currency.current_price,  # Рассчитываем сумму в целевой валюте
        commission_amount=amount_base * exchange_pair.commission_rate / 100,  # Рассчитываем комиссию
        status='pending'
    )
    return transaction


def update_transaction_status(transaction, new_status):
    # Обновляем статус транзакции
    transaction.status = new_status
    transaction.save()  # Сохраняем изменения
    return transaction



def exchange_currency(user, base_currency, target_currency, amount_base):
    """
    Функция для обмена криптовалюты.
    """
    # Проверяем, что входные данные корректны
    if amount_base <= 0:
        raise ValueError("Сумма для обмена должна быть положительной")
    
    # Находим соответствующую пару обмена
    try:
        exchange_pair = ExchangePair.objects.get(
            base_currency=base_currency,
            target_currency=target_currency
        )
    except ExchangePair.DoesNotExist:
        raise ValueError("Пара обмена не найдена")

    # Рассчитываем сумму в целевой валюте
    amount_target = amount_base * exchange_pair.target_currency.current_price

    # Рассчитываем комиссию
    commission_amount = amount_base * exchange_pair.commission_rate / 100

    # Создаем транзакцию для обмена
    transaction = Transaction.objects.create(
        user=user,
        exchange_pair=exchange_pair,
        amount_base=amount_base,
        amount_target=amount_target,
        commission_amount=commission_amount,
        status='pending'
    )

    return transaction

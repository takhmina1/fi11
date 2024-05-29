from .models import Wallet, Transaction
from django.db.models import F

def make_transaction(sender_wallet_name, receiver_wallet_name, amount):
    # Пытаемся получить объекты кошельков отправителя и получателя по их именам
    try:
        sender_wallet = Wallet.objects.get(name=sender_wallet_name)
        receiver_wallet = Wallet.objects.get(name=receiver_wallet_name)
    except Wallet.DoesNotExist:
        # В случае, если кошелек не найден, возвращаем ошибку
        return False, "Ошибка: Один из кошельков не найден."

    # Проверяем, достаточно ли средств на кошельке отправителя для проведения транзакции
    if sender_wallet.balance < amount:
        return False, "Ошибка: Недостаточно средств на кошельке отправителя."

    # Создаем запись о транзакции в базе данных
    transaction = Transaction.objects.create(sender=sender_wallet, receiver=receiver_wallet, amount=amount)
    # Обновляем балансы кошельков отправителя и получателя
    sender_wallet.balance = F('balance') - amount
    receiver_wallet.balance = F('balance') + amount
    sender_wallet.save()
    receiver_wallet.save()

    return True, "Транзакция успешно выполнена."

def get_wallet_balance(wallet_name):
    # Пытаемся получить объект кошелька по его имени
    try:
        wallet = Wallet.objects.get(name=wallet_name)
        # Если кошелек найден, возвращаем его баланс
        return True, wallet.balance
    except Wallet.DoesNotExist:
        # В случае, если кошелек не найден, возвращаем ошибку
        return False, "Ошибка: Кошелек не найден."

def create_wallet(name, balance, send_type, receive_type, commission):
    # Пытаемся создать новый кошелек с указанными параметрами
    try:
        wallet = Wallet.objects.create(name=name, balance=balance, send_type=send_type, receive_type=receive_type, commission=commission)
        return True, f"Кошелек {name} успешно создан."
    except Exception as e:
        # В случае возникновения ошибки при создании кошелька, возвращаем сообщение об ошибке
        return False, f"Ошибка при создании кошелька: {str(e)}"

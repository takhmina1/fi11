from django.db import models
from django.contrib.auth.models import User

class CryptoWallet(models.Model):
    """
    Модель для криптовалютного кошелька пользователя.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='crypto_wallet')
    currency = models.ForeignKey('CryptoCurrency', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=8, default=0)

    def __str__(self):
        return f"{self.user.username}'s {self.currency.symbol} Wallet"

    def deposit(self, amount):
        """
        Метод для пополнения баланса криптовалютного кошелька.
        """
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        """
        Метод для снятия средств с криптовалютного кошелька.
        """
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")

class FiatWallet(models.Model):
    """
    Модель для фиатного кошелька пользователя.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fiat_wallet')
    currency = models.CharField(max_length=3)  # Например, USD, EUR и т.д.
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s {self.currency} Wallet"

    def deposit(self, amount):
        """
        Метод для пополнения баланса фиатного кошелька.
        """
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        """
        Метод для снятия средств с фиатного кошелька.
        """
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")

class CryptoCurrency(models.Model):
    """
    Модель для криптовалют.
    """
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    current_price = models.DecimalField(max_digits=15, decimal_places=8)  # Текущая цена криптовалюты

    def __str__(self):
        return self.name

class ExchangePair(models.Model):
    """
    Модель для пар обмена криптовалюты.
    """
    base_currency = models.ForeignKey(CryptoCurrency, related_name='base_currency', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(CryptoCurrency, related_name='target_currency', on_delete=models.CASCADE)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Комиссия за обмен в процентах

    def __str__(self):
        return f"{self.base_currency.symbol}/{self.target_currency.symbol}"

class Transaction(models.Model):
    """
    Модель для транзакций.
    """

    user = models.ForeignKey(User, related_name='balanse_transactions', on_delete=models.CASCADE)
    exchange_pair = models.ForeignKey(ExchangePair, on_delete=models.CASCADE)
    amount_base = models.DecimalField(max_digits=15, decimal_places=8)  # Сумма в базовой валюте
    amount_target = models.DecimalField(max_digits=15, decimal_places=8)  # Сумма в целевой валюте
    commission_amount = models.DecimalField(max_digits=15, decimal_places=8)  # Сумма комиссии
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')

    def save(self, *args, **kwargs):
        """
        Переопределенный метод для сохранения транзакции и автоматического расчета суммы в целевой валюте и комиссии.
        """
        if not self.pk:
            self.amount_target = self.calculate_target_amount()
            self.commission_amount = self.calculate_commission()
        super().save(*args, **kwargs)

    def calculate_target_amount(self):
        """
        Метод для расчета суммы в целевой валюте.
        """
        target_price = self.exchange_pair.target_currency.current_price
        amount_target = self.amount_base * target_price
        return amount_target

    def calculate_commission(self):
        """
        Метод для расчета комиссии в базовой валюте.
        """
        commission_rate = self.exchange_pair.commission_rate
        commission_amount = (self.amount_base * commission_rate) / 100
        return commission_amount

    def __str__(self):
        return f"{self.user.username} - {self.amount_base} {self.exchange_pair}"

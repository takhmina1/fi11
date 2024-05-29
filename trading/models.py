from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cryptocurrency(models.Model):
    # Модель для криптовалюты, хранит информацию о ней
    name = models.CharField(max_length=100)  # Название криптовалюты
    currency_code = models.CharField(max_length=10)  # Код валюты
    symbol = models.CharField(max_length=10)  # Символьный код криптовалюты
    country = models.CharField(max_length=100)  # Страна
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)  # Курс обмена
    market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # Рыночная капитализация

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    # Модель для портфеля пользователя, хранит информацию о криптовалюте в портфеле
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
    amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты в портфеле

    def __str__(self):
        return f'{self.user.username} - {self.cryptocurrency.name}'

class Order(models.Model):
    # Типы ордеров
    ORDER_TYPES = (
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
        ('exchange', 'Обмен'),  # Добавляем тип ордера для обмена
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    order_type = models.CharField(max_length=8, choices=ORDER_TYPES)  # Увеличиваем длину поля для типа ордера
    created_at = models.DateTimeField(default=timezone.now)
    exchange_currency = models.CharField(max_length=10, blank=True, null=True)  # Добавляем поле для валюты обмена

    # Добавляем поля для комиссии
    commission_currency = models.CharField(max_length=10, blank=True, null=True)  # Валюта комиссии
    commission_type = models.CharField(max_length=10, blank=True, null=True)  # Тип комиссии (проценты или фиксированная сумма)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=4, default=0.01, blank=True, null=True)  # Ставка комиссии

    def __str__(self):
        return f'{self.user.username} - {self.order_type} - {self.amount} {self.cryptocurrency.symbol}'




    def calculate_commission(self, total_amount):
        if self.commission_type and self.commission_rate:
            if self.commission_type == 'percent':
                return total_amount * self.commission_rate
            elif self.commission_type == 'fixed':
                return self.commission_rate
        else:
            return 0  

    

    # Метод для выполнения ордера
    def execute_order(self):
        total_cost = self.amount * self.price
        # Вычисляем комиссию, если она указана
        commission = self.calculate_commission(total_cost)
        total_cost_with_commission = total_cost + commission

        if self.order_type == 'buy':
            # Логика для покупки криптовалюты
            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            portfolio.amount += self.amount
            portfolio.save()
            # Корректировка баланса пользователя на основе цены ордера с учетом комиссии
            self.user.profile.balance -= total_cost_with_commission
            self.user.profile.save()
        elif self.order_type == 'sell':
            # Логика для продажи криптовалюты
            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            if portfolio.amount >= self.amount:
                portfolio.amount -= self.amount
                portfolio.save()
                # Корректировка баланса пользователя на основе цены ордера с учетом комиссии
                self.user.profile.balance += total_cost - commission
                self.user.profile.save()
            else:
                raise ValueError("Недостаточно криптовалюты в портфеле для выполнения ордера на продажу")


class Trade(models.Model):
    # Типы сделок (покупка или продажа)
    TRADE_TYPES = (
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
    )

    # Пользователь, совершающий сделку
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Криптовалюта, объект которой участвует в сделке
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    
    # Количество криптовалюты, участвующее в сделке
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    
    # Цена одной единицы криптовалюты при сделке
    price = models.DecimalField(max_digits=20, decimal_places=10)
    
    # Тип сделки (покупка или продажа)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    
    # Время совершения сделки
    timestamp = models.DateTimeField(auto_now_add=True)

    # Валюта, в которой выражается комиссия за сделку
    commission_currency = models.CharField(max_length=10)

    # Тип комиссии (проценты или фиксированная сумма)
    commission_type = models.CharField(max_length=10)

    # Ставка комиссии для покупок
    buy_commission_rate = models.DecimalField(max_digits=5, decimal_places=4, default=0.01)
    
    # Ставка комиссии для продаж
    sell_commission_rate = models.DecimalField(max_digits=5, decimal_places=4, default=0.015)
    
    # Дополнительные услуги, предоставляемые при совершении сделки
    additional_services = models.CharField(max_length=100, blank=True, null=True)
    
    # Показатель конкурентоспособности комиссии
    competitiveness = models.BooleanField(default=True)
    
    # Показатель регулирования комиссии
    regulation = models.BooleanField(default=False)

    # Валюта для обмена
    exchange_currency = models.CharField(max_length=10)

    # Метод для выполнения сделки
    def execute_trade(self):
        # Логика для совершения покупки или продажи криптовалюты
        if self.trade_type == 'buy':
            total_cost = self.amount * self.price
            commission = self.calculate_commission(total_cost)
            total_cost_with_commission = total_cost + commission

            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            portfolio.amount += self.amount
            portfolio.save()

            self.user.profile.balance -= total_cost_with_commission
            self.user.profile.save()
        elif self.trade_type == 'sell':
            total_gain = self.amount * self.price
            commission = self.calculate_commission(total_gain)
            total_gain_with_commission = total_gain - commission

            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            if portfolio.amount >= self.amount:
                portfolio.amount -= self.amount
                portfolio.save()

                self.user.profile.balance += total_gain_with_commission
                self.user.profile.save()
            else:
                raise ValueError("Недостаточно криптовалюты в портфеле для выполнения ордера на продажу")

    # Метод для расчета комиссии
    def calculate_commission(self, total_amount):
        if self.trade_type == 'buy':
            base_commission_rate = self.buy_commission_rate
        else:
            base_commission_rate = self.sell_commission_rate

        additional_fee = 0
        if self.competitiveness:
            additional_fee = total_amount * 0.002  # Дополнительная комиссия для поддержания конкурентоспособности

        regulatory_fee = 0
        if self.regulation:
            regulatory_fee = total_amount * 0.001  # Регулировочная комиссия

        commission = base_commission_rate * total_amount + additional_fee + regulatory_fee
        return commission



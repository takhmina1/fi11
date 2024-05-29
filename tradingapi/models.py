from django.db import models

class Currency(models.Model):
    currency_code = models.CharField(max_length=10, unique=True)
    currency_name = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency_name} ({self.currency_code})"

class CryptoCurrency(models.Model):
    currency_code = models.CharField(max_length=10, unique=True)
    currency_name = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency_name} ({self.currency_code})"

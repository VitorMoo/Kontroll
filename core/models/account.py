from decimal import Decimal
from django.utils import timezone
from django.db import models
from core.models import User
from django.core.validators import RegexValidator

class Account(models.Model):

    class AccountType(models.TextChoices):
        CHECKING = 'Current'
        SAVINGS = 'Savings'
        CREDIT_CARD = 'Credit Card'
        INVESTMENT = 'Investment'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    type = models.CharField(max_length=50, choices=AccountType.choices, default=AccountType.CHECKING)
    opening_date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal(0.00))
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3, default="BRL",validators=[RegexValidator(r"^[A-Z]{3}$")])
    is_archived  = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=250, default='')

    class Meta:
        verbose_name = ('Account')
        verbose_name_plural = ('Accounts')
        unique_together = ("user", "name")
        ordering = ("name",)
        indexes = [
            models.Index(fields=['user', 'name']),
        ]

    def __str__(self):
        return f"{self.name} – {self.user.username}"


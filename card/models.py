from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime, timedelta


def get_default_end_activity_date():
    """By default, set to end_activity_date field 1 year after card create"""
    return datetime.now() + timedelta(days=365)


class Card(models.Model):
    """Create Card model"""
    STATUS_CHOICES = [
        ('not_activated', 'Не активирована'),
        ('activated', 'Активирована'),
        ('expired', 'Просрочена'),
    ]

    objects = models.Manager()

    card_series = models.CharField(max_length=4, verbose_name='Серия карты')
    card_number = models.BigIntegerField(unique=True, verbose_name='Номер карты')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска')
    end_activity_date = models.DateTimeField(default=get_default_end_activity_date,
                                             verbose_name='Дата окончания активности')
    use_date = models.DateTimeField(auto_now=True, verbose_name='Дата использования')
    total = models.DecimalField(default=0.00, max_digits=12, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))], verbose_name='Сумма')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,
                              default='not_activated', verbose_name='Статус карты')

    class Meta:
        verbose_name = 'Карту'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return f'{self.card_series} {self.card_number}'

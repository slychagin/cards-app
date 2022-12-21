from django.db import models


class Card(models.Model):
    objects = models.Manager()

    card_series = models.CharField(max_length=4, verbose_name='Серия карты')
    card_number = models.BigIntegerField(unique=True, verbose_name='Номер карты')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска')
    end_activity_date = models.DateTimeField(verbose_name='Дата окончания активности')
    use_date = models.DateTimeField(auto_now=True, verbose_name='Дата использования')
    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма')
    not_activated = models.BooleanField(default=True, verbose_name='Не активирована')
    activated = models.BooleanField(verbose_name='Активирована')
    expired = models.BooleanField(verbose_name='Просрочена')

    def __str__(self):
        return f'{self.card_series}{self.card_number}'

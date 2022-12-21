from django.contrib import admin
from card.models import Card


class CardAdmin(admin.ModelAdmin):
    """Show Card model data in admin panel"""
    list_display = (
        'card_series',
        'card_number',
        'created_date',
        'end_activity_date',
        'use_date',
        'total',
        'status'
    )
    list_per_page = 20
    list_max_show_all = 100


admin.site.register(Card, CardAdmin)

from django import template


register = template.Library()


@register.filter(name='get_index')
def get_index(card_list, i):
    return card_list[i]

from django.shortcuts import render

from card.models import Card


def cards_list(request):
    """Render home page. Show card list"""
    all_cards = Card.objects.filter()
    cards_idx = [i + 1 for i, card in enumerate(all_cards)]

    context = {
        'user': request.user,
        'all_cards': all_cards,
        'cards_idx': cards_idx,
    }
    return render(request, 'cards_list.html', context)


def card_generator(request):
    """Generate cards"""

    return render(request, 'card_generator.html')


def card_profile(request):
    """Render card profile page"""
    return render(request, 'card_profile.html')

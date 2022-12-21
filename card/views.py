from django.shortcuts import render


def cards_list(request):
    """Render home page. Show card list"""
    return render(request, 'cards_list.html')


def card_generator(request):
    """Generate cards"""
    return render(request, 'card_generator.html')

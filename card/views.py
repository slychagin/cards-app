import random
from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from card.forms import CardGenerateForm
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
    if request.method == 'POST':
        form = CardGenerateForm(request.POST)
        if form.is_valid():
            card_series = form.cleaned_data['card_series'].upper()
            digits_number = int(form.cleaned_data['digits_number'])
            card_number = int(form.cleaned_data['card_number'])
            term_activity = form.cleaned_data['term_activity']

            card_nums = generate_card_numbers(card_series, digits_number, card_number)

            for number in card_nums:
                card = Card(
                    card_series=card_series,
                    card_number=number,
                    end_activity_date=datetime.now() + timedelta(days=int(term_activity))
                )
                card.save()

            if len(card_nums) < card_number:
                available_quantity = card_number - len(card_nums)
                messages.info(request, f'Для данной серии было сгенерировано {available_quantity} карт.\n'
                                       f'Для оставшихся {card_number - available_quantity} карт установите другую серию.')

            messages.success(request, 'Карты успешно добавлены в базу данных!')
            return redirect('card_generator')
        else:
            messages.error(request, form.non_field_errors())
    else:
        form = CardGenerateForm()

    context = {
        'form': form
    }
    return render(request, 'card_generator.html', context)


def card_profile(request):
    """Render card profile page"""
    return render(request, 'card_profile.html')


def generate_card_numbers(card_series, digits_number, card_number):
    """
    Generates a list of card numbers depending on
    the number of cards entered by the user
    """
    cards = Card.objects.filter(card_series=card_series)
    existing_card_numbers = [card.card_number for card in cards]

    lower_range_limit = int('1' + '0'*(digits_number - 1))
    upper_range_limit = int('9'*digits_number)

    cards_numbers = random.sample(range(lower_range_limit, upper_range_limit + 1), card_number)
    unique_card_numbers = [num for num in cards_numbers if num not in existing_card_numbers]

    return unique_card_numbers

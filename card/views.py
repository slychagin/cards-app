import random
from datetime import datetime, timedelta, timezone
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from card.forms import CardGenerateForm
from card.models import Card


def cards_list(request):
    """Render home page. Show card list"""
    cards = Card.objects.filter().order_by('-created_date')
    cards_idx = [i + 1 for i, card in enumerate(cards)]

    # update card status if term_activity grater than current date
    now = datetime.now(timezone.utc)

    for card in cards:
        if card.end_activity_date < now:
            card.status = 'expired'
            card.save()

    context = {
        'user': request.user,
        'cards': cards,
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


def card_profile(request):
    """Render card profile page"""



    return render(request, 'card_profile.html')


def delete_card(request, card_id):
    """Delete chose card"""
    if request.user.is_authenticated:
        card = Card.objects.get(id=card_id)
        card.delete()
        return redirect('cards_list')
    else:
        messages.error(request, 'Чтобы удалить карту, войдите в систему!')
        return redirect('cards_list')


def activate_card(request, card_id):
    """Activate or deactivate card"""
    if request.user.is_authenticated:
        card = Card.objects.get(id=card_id)
        card_status = card.status

        if card_status == 'activated':
            card.status = 'not_activated'
        else:
            card.status = 'activated'
        card.save()

        return redirect('cards_list')
    else:
        messages.error(request, 'Чтобы изменить статус карты, войдите в систему!')
        return redirect('cards_list')


def search(request):
    """Search card by keyword"""
    all_cards = None
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            cards = Card.objects.order_by('-created_date').filter(
                Q(card_series__icontains=query) |
                Q(card_number__icontains=query) |
                Q(created_date__icontains=query) |
                Q(end_activity_date__icontains=query) |
                Q(status__icontains=query)
            )
            cards_idx = [i + 1 for i, card in enumerate(cards)]
        if not query:
            return redirect('cards_list')

    context = {
        'cards': cards,
        'cards_idx': cards_idx
    }
    return render(request, 'cards_list.html', context)

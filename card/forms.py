from django import forms
from string import ascii_letters, digits
from card.models import Card


TERM_CHOICES = (
    ('365', '1 год'),
    ('183', '6 месяцев'),
    ('30', '1 месяц')
)


class CardGenerateForm(forms.ModelForm):
    digits_number = forms.IntegerField(min_value=4, max_value=16)
    card_number = forms.IntegerField(min_value=1, max_value=1000)
    term_activity = forms.ChoiceField(choices=TERM_CHOICES)

    class Meta:
        model = Card
        fields = ('card_series', 'digits_number', 'card_number', 'term_activity')

    def __init__(self, *args, **kwargs):
        super(CardGenerateForm, self).__init__(*args, **kwargs)
        self.fields['card_series'].widget.attrs['placeholder'] = 'Кол-во знаков от 2 до 4'
        self.fields['digits_number'].widget.attrs['placeholder'] = 'Кол-во цифр от 4 до 16'
        self.fields['card_number'].widget.attrs['placeholder'] = 'Кол-во карт от 1 до 1000'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['term_activity'].widget.attrs['class'] = 'form-select'

    def clean(self):
        """Validate card_series field"""
        cleaned_data = super(CardGenerateForm, self).clean()
        card_series = cleaned_data.get('card_series')

        if len(card_series) < 2:
            raise forms.ValidationError('Кол-во букв или цифр в поле серия карт должно быть от 2-х до 4-х')

        for symbol in card_series:
            if symbol not in get_card_series_symbols():
                raise forms.ValidationError('Серия карты должна содержать латинские, русские буквы или цифры')


def get_card_series_symbols():
    """Return a string of symbols for validate card_series field"""
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
    card_series_symbols = cyrillic_letters + ascii_letters + digits
    return card_series_symbols

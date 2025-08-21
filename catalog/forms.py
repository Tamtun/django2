from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control-file'
            elif isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']

    def clean_name(self):
        name = self.cleaned_data.get('name', '').lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError(f"Название содержит запрещённое слово: «{word}»")
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data.get('description', '').lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError(f"Описание содержит запрещённое слово: «{word}»")
        return self.cleaned_data['description']

    def clean_purchase_price(self):
        price = self.cleaned_data.get('purchase_price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

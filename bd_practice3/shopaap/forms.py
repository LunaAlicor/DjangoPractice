from django import forms
from .models import Product, Orders


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'description', 'price', 'discount'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Имя должно содержать как минимум 3 символа.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 50 or len(description) >= 100:
            raise forms.ValidationError("Описание должно быть от 50 до 100 символов")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 10 or price > 25000:
            raise forms.ValidationError("Цена должна быть больше 10 и меньше 25000")

        return price

    def clean_discount(self):
        discount = self.cleaned_data.get('discount')

        if discount < 0 or discount > 90:
            raise forms.ValidationError("Скидка должна быть от 0 до 90")
        return discount


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['delivery_address', 'promocode', 'products']

    def clean_delivery_address(self):
        delivery_address = self.cleaned_data.get('delivery_address')
        if len(delivery_address) > 50:
            raise forms.ValidationError('Адрес должен быть не длинее 50 символов')
        return delivery_address

    def clean_promocode(self):
        promocode = self.cleaned_data.get('promocode')

        if promocode != ('' or 'luna' or None):
            raise forms.ValidationError('Есть только один промокод luna')

        return promocode

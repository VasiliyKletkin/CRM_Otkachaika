from addresses.utils import get_or_create_address, get_address
from dal import autocomplete
from django import forms

from .models import Address, City, Country, Region, Street


class CountyForm(forms.ModelForm):
    def clean(self):
        name = self.cleaned_data['name']
        if Country.objects.filter(name=name).exists():
            raise forms.ValidationError('Такая страна уже существует')
        return super().clean()

    class Meta:
        model = Country
        fields = ('__all__')


class RegionForm(forms.ModelForm):
    def clean(self):
        country = self.cleaned_data['country']
        name = self.cleaned_data['name']
        if Region.objects.filter(country_id=country, name=name).exists():
            raise forms.ValidationError('Такой регион уже существует')
        return super().clean()

    class Meta:
        model = Region
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
        }


class CityForm(forms.ModelForm):
    def clean(self):
        region = self.cleaned_data['region']
        name = self.cleaned_data['name']
        if City.objects.filter(region_id=region, name=name).exists():
            raise forms.ValidationError('Такой город уже существует')
        return super().clean()

    class Meta:
        model = City
        fields = ('__all__')
        widgets = {
            'region': autocomplete.ModelSelect2(url='region-autocomplete'),
        }


class StreetForm(forms.ModelForm):
    def clean(self):
        city = self.cleaned_data['city']
        name = self.cleaned_data['name']
        if Street.objects.filter(city_id=city, name=name).exists():
            raise forms.ValidationError('Такая улица уже существует')
        return super().clean()

    class Meta:
        model = Street
        fields = ('__all__')
        widgets = {
            'city': autocomplete.ModelSelect2(url='city-autocomplete'),
        }


class AddressForm(forms.ModelForm):
    def clean(self):
        home = self.cleaned_data['home']
        street = self.cleaned_data['street']
        if Address.objects.filter(street_id=street, home=home).exists():
            raise forms.ValidationError('Такой адрес уже существует')
        self.cleaned_data['home'] = self.cleaned_data['home'].upper()
        return super().clean()

    class Meta:
        model = Address
        fields = ('__all__')
        widgets = {
            'street': autocomplete.ModelSelect2(url='street-autocomplete', attrs={'data-minimum-input-length': 3}),
        }


class AddressModelChoiceFromListField(forms.ModelChoiceField):

    def __init__(self, create=False, *args, **kwargs):
        self.create = create
        kwargs['widget'] = autocomplete.ListSelect2(url='dadata-address-autocomplete')
        kwargs['queryset'] = Address.objects.all()
        super().__init__(*args, **kwargs)

    def clean(self, value):
        try:
            value = get_or_create_address(value) if self.create else get_address(value)
            return super().clean(value)
        except Exception:
            raise forms.ValidationError("Невозможно выбрать данный адрес")

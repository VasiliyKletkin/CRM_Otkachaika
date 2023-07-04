from django.urls import path

from .views import (AddressAutocomplete, CityAutocomplete, CountryAutocomplete,
                    RegionAutocomplete, StreetAutocomplete, DadataAddressListAutocomplete)

urlpatterns = [
     path('country-autocomplete/', CountryAutocomplete.as_view(),
         name='country-autocomplete'),
     path('region-autocomplete/', RegionAutocomplete.as_view(),
         name='region-autocomplete'),
     path('city-autocomplete/', CityAutocomplete.as_view(),
         name='city-autocomplete'),
     path('street-autocomplete/', StreetAutocomplete.as_view(),
         name='street-autocomplete'),
    path('address-autocomplete/', AddressAutocomplete.as_view(),
         name='address-autocomplete'),
     path('dadata-address-autocomplete/', DadataAddressListAutocomplete.as_view(),
         name='dadata-address-autocomplete'),
]

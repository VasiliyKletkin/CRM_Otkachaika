from django.urls import include, path
from rest_framework import routers

from .views import CompanyAutocomplete, ServiceCompanyAutocomplete

router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('company-autocomplete/', CompanyAutocomplete.as_view(),
         name='company-autocomplete'),
    path('servicecompany-autocomplete/', ServiceCompanyAutocomplete.as_view(),
         name='servicecompany-autocomplete'),
]

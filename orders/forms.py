from django import forms
from .models import Order
from localflavor.us.forms import USZipCodeField
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', _('postal_code'), 'city']



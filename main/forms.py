from django import forms
from .models import departments


class main_form(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    date = forms.DateField(required=True)
    department = forms.ModelChoiceField(
        queryset=departments.objects.all(),
        required=False,
    )

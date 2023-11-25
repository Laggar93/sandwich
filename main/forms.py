from django import forms

YES_NO_CHOICES = [('1', 'Первый отдел'),
    ('2', 'Второй отдел'), ('3', 'Третий отдел')]


class main_form(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    date = forms.DateField(required=True)
    department = forms.ChoiceField(label="departments", choices=YES_NO_CHOICES)

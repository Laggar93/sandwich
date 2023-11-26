from django import forms

CHOICES = [('1', 'Первый отдел'),
    ('2', 'Второй отдел'), ('3', 'Третий отдел')]


class main_form(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    date = forms.DateField(required=True)
    department = forms.ChoiceField(label="department", choices=CHOICES)

    def clean_department(self):
        selected_display_name = self.cleaned_data['department']
        for val, disp_name in CHOICES:
            if disp_name == selected_display_name:
                return val
        return selected_display_name

from django import forms
from .models import Wine


class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to each field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
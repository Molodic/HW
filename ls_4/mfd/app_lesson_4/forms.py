from django import forms
from .models import Advertisement
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class AdvertisementForm(forms.ModelForm):
    regularExpressionForTitle = r"[!@#$%^:;&?*()_=+\\|/.,<>~`'\"]"

    title = forms.CharField(label="Заголовок", max_length=64, widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
                            validators = [RegexValidator(regex=regularExpressionForTitle, inverse_match=True, message=_("В названии спец-символ."))])
    class Meta:
        model = Advertisement
        fields = ["title", "description", "price", "tradePossibility", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-lg"}), #Overload later
            "description": forms.Textarea(attrs={"class": "form-control form-control-lg", "rows": 3, "style":"max-width: max-content"}),
            "price": forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
            "tradePossibility": forms.CheckboxInput(attrs={"class": "form-check-input"}), 
            "image": forms.FileInput(attrs={"class": "form-control form-control-lg"})
        }
        help_texts = {
            "tradePossibility" : None
        }

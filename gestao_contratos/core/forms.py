from django import forms

from gestao_contratos.core.models import Athlete


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'email', 'cpf', 'rg']

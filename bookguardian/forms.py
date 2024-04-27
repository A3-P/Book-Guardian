from django import forms


class PositionForm(forms.Form):
    position = forms.CharField()

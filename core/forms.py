from django import forms
from django.contrib.auth.models import User
from .models import Owner, Animal, Vaccination


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'phone', 'address']


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'breed', 'age']


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ['animal', 'vaccine_name', 'date_given', 'next_due', 'notes']
        widgets = {
            'date_given': forms.DateInput(attrs={'type': 'date','placeholder': 'Select vaccination date'}),
            'next_due': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        if owner:
            self.fields['animal'].queryset = Animal.objects.filter(owner=owner)



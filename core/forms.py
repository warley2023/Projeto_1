from django import forms
from django.contrib.auth.forms import UserCreationForm

class CadastroForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields
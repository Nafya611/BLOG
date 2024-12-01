from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(UserCreationForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    username=forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
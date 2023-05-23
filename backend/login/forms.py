from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Custom createuserform 
class CreateUserForm(UserCreationForm):

    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            # 'class': 'form-control',
            'placeholder': '使用者名稱',
            })
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            # 'class': 'form-control',
            'placeholder': '電子信箱',
            })
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            # 'class': 'form-control',
            'placeholder': '密碼',
            })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            # 'class': 'form-control',
            'placeholder': '請再輸入一次密碼',
            })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


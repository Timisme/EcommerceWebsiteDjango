from django.forms import EmailInput, ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        labels = {
            'name':'',
            'email':'',
            'subject':'',
            'message':'',
        }
        widgets = {
            'name': forms.TextInput(attrs= {
                # 'class': 'form-control',
                'placeholder': '姓名',
            }),
            'email': forms.EmailInput(attrs= {
                # 'class': 'form-control',
                'placeholder': '電子郵件',
            }),
            'subject': forms.TextInput(attrs= {
                # 'class': 'form-control',
                'placeholder': '主題',
            }), 
            'message': forms.Textarea(attrs= {
                # 'class': 'form-control',
                'cols': "30",
                'rows': "10",
                'placeholder': '訊息', 
            }),
        }

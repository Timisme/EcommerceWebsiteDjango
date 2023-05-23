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
                'placeholder': 'YOUR NAME',
            }),
            'email': forms.EmailInput(attrs= {
                # 'class': 'form-control',
                'placeholder': 'YOUR E-MAIL',
            }),
            'subject': forms.TextInput(attrs= {
                # 'class': 'form-control',
                'placeholder': 'SUBJECT',
            }), 
            'message': forms.Textarea(attrs= {
                # 'class': 'form-control',
                'cols': "30",
                'rows': "10",
                'placeholder': 'MESSAGE', 
            }),
        }

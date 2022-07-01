from email.message import Message
from django import forms
from .models import *

class MailForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'


    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),max_length=100,min_length=10,required=True)
    Email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),max_length=100,min_length=10,required=True)
    Subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),max_length=100,min_length=10,required=True)
    Text_Message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}),max_length=400,min_length=10,required=True)
    
   
  
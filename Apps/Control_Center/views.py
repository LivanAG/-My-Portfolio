from email import message
from django.shortcuts import render

from lib2to3.pgen2 import token
from django.db.models.functions import Coalesce
from operator import invert
from re import template
from django.views.generic import TemplateView,FormView,ListView,CreateView,DeleteView,DetailView
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf  import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls  import reverse_lazy
from django.shortcuts import render,redirect
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from django.conf import settings


# Create your views here.

def send_email(Email,Subject,Text_Message):
        try:
            
            
            #We establish connection with the gmail smtp server
            mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
            print(mailServer.ehlo())# Check if we have connection and give us the answer 
            mailServer.starttls() # Establish a secure connection
            print(mailServer.ehlo())# Check if we have connection and give us the answer 
            mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)

            email_to=settings.EMAIL_HOST_USER
            
            # We build the message
            email_message = MIMEText(Text_Message)
            email_message['From']=settings.EMAIL_HOST_USER
            email_message['To']=settings.EMAIL_HOST_USER
            email_message['Subject']=Subject
        
            # Sending the message
            mailServer.sendmail(Email,email_to,email_message.as_string())

            
        except Exception as e:
            print(e)



#Index
class IndexView (FormView):
    template_name= 'Control_Center/index.html'
    form_class= MailForm

    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        form = self.get_form()

        try:
            if form.is_valid():
                Name= form.cleaned_data['Name']
                Email= form.cleaned_data['Email']
                Subject= form.cleaned_data['Subject']
                

                Text_Message = form.cleaned_data['Text_Message'] + "\n\nEste correo fue enviado por \nNombre: " + form.cleaned_data['Name'] + "\nEmail: " +form.cleaned_data['Email']

                send_email(Email,Subject,Text_Message)
                
            else:
                data['error']=form.errors

        except Exception as e:
            data['error']=str(e)
        
        return JsonResponse(data)


 

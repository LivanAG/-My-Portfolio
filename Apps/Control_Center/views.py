from django.shortcuts import render

from lib2to3.pgen2 import token
from django.db.models.functions import Coalesce
from operator import invert
from re import template
from django.views.generic import TemplateView,FormView,ListView,CreateView,DeleteView,DetailView
from .models import *
#from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf  import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls  import reverse_lazy
from django.shortcuts import render,redirect
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Create your views here.


#Index
class IndexView (TemplateView):
    template_name= 'Control_Center/index.html'


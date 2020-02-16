from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'
    
    title= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Add new task'}))

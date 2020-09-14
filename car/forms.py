from django import forms
from .models import *


class Apply_job (forms.ModelForm):
    class Meta:
        model = Apply_For
        fields = ['name', 'email', 'link', 'cv', 'coverL']





class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'owner')



class Bid_price_Form(forms.ModelForm):
    class Meta:
        model = Bid_price
        fields = ['bid_price']
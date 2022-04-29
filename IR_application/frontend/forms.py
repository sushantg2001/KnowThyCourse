from cProfile import label
from django import forms

class queryForm(forms.Form):
    query = forms.CharField(label='Search', max_length=1000, required=True)

from cProfile import label
from django import forms

class queryForm(forms.Form):
    query = forms.CharField(label='Input Your query', max_length=1000, required=True)

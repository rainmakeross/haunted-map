__author__ = 'derya'
# forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField()


__author__ = 'derya'
# forms.py
from django import forms
from models import Newsletter

class NewsletterForm(forms.Form):
    email = forms.CharField()

    def save_email(self):
        Newsletter.email = ''


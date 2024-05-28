from django import forms
from django.shortcuts import render
from django.shortcuts import requests

def submission(request):
    fname = forms.CharField(max_length=200)
    lname = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    message = forms.CharField(max_length=500)
    return render(request, "message.html", context)
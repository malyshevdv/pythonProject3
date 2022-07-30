from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
# Create your views here.

def showAnswer(request):
    HttpRequest('About book')

class AboutClass(TemplateView):
    template_name = 'about.html'


class MyProfile(TemplateView):
    template_name = 'profile.html'
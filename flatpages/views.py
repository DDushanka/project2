from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django import template
from django.http import HttpResponse
def home(request):
 return HttpResponse(u'Hello World!', content_type="text/plain")
def home(request):
 return render(request, 'templates/index.html')

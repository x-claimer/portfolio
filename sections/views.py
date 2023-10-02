from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def view_function(request):
#     return HttpResponse("Hello Ateeq!!")

def view_function(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

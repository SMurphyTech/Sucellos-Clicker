from django.shortcuts import render 

# Fetch response
from django.http import JsonResponse

from .models import Clicks

# Create your views here.
def index(request):
  # Gets or creates record and returns a tuple (object, bool)
  clicks = Clicks.objects.get_or_create(pk=1)[0] # returns the model object
  return render(request, 'clicker/index.html', { "clicked" : clicks.clicked })

# REST API views
def increase(request):
  if(request.method == "POST"):
    clicks = Clicks.objects.get_or_create(pk=1)[0]
    clicks.clicked += 1
    clicks.save()

    return JsonResponse({ "clicked" : clicks.clicked })
  else:
    return render(request, "clicker/404.html")

def decrease(request):
  if(request.method == "POST"):
    clicks = Clicks.objects.get_or_create(pk=1)[0]
    clicks.clicked -= 1
    clicks.save()

    return JsonResponse({ "clicked" : clicks.clicked })
  else:
    return render(request, "clicker/404.html")

def update(request):
  clicks = Clicks.objects.get_or_create(pk=1)[0]
  return JsonResponse({ "clicked" : clicks.clicked })
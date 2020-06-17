from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact



def index(request):
    context = Contact.objects.all()
    print(context)
    return render(request, 'contacttracer/index.html', {'context':context})
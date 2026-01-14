from django.shortcuts import render

def workshop(request):
    return render(request, 'workshops/workshop.html',)

def form(request):
    return render(request, 'workshops/form.html',)

# Create your views here.

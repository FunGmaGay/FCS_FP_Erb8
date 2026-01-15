from django.shortcuts import render

def workshop(request):
    return render(request, 'workshops/workshop.html',)

def form(request):
    return render(request, 'workshops/form.html',)

def tutor1(request):
    return render(request, 'workshops/tutor1.html',)

def tutor2(request):
    return render(request, 'workshops/tutor2.html',)

# Create your views here.

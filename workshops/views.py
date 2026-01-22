from django.shortcuts import render, get_object_or_404
from workshops.models import Workshop

def workshop(request):
    return render(request, 'workshops/workshop.html',)

#def form(request):
    #return render(request, 'workshops/form.html',)

def urdu(request):
    workshop = get_object_or_404(Workshop, pk=1)
    context = {"workshop":workshop}
    return render(request, 'workshops/urdu.html', context)

def milktea(request):
    
    return render(request, 'workshops/milktea.html',)

def henna(request):
    return render(request, 'workshops/henna.html',)

# Create your views here.

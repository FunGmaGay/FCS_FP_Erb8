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
    workshop = get_object_or_404(Workshop, pk=2)
    context = {"workshop":workshop}
    return render(request, 'workshops/milktea.html', context)

def henna(request):
    workshop = get_object_or_404(Workshop, pk=3)
    context = {"workshop":workshop}
    return render(request, 'workshops/henna.html', context)

# Create your views here.

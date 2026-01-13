from django.shortcuts import render

def contact(request):
    return render(request, 'supports/contact.html',)

def donation(request):
    return render(request, 'supports/donation.html',)

def support(request):
    return render(request, 'supports/support.html',)


# Create your views here.

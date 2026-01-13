from django.shortcuts import render

def activity(request):
    return render(request, 'kyks/activity.html',)

def album1(request):
    return render(request, 'kyks/album1.html',)

def album2(request):
    return render(request, 'kyks/album2.html',)

def kyk(request):
    return render(request, 'kyks/kyk.html',)

def media(request):
    return render(request, 'kyks/media.html',)

def news(request):
    return render(request, 'kyks/news.html',)

# Create your views here.

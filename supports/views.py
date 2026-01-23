import io
from django.http import FileResponse, HttpResponse, JsonResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, A6, letter, landscape
from django.conf import settings
import os


import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from django.shortcuts import render

def contact(request):
    return render(request, 'supports/contact.html',)

def donation2(request):
    first_name=''
    last_name=''
    email=''
    if 'first_name' in request.POST:
        first_name = request.POST["first_name"]
    if 'last_name' in request.POST:
        last_name = request.POST["last_name"]
    if 'email' in request.POST:
        email = request.POST["email"]

    buffer = io.BytesIO()
    img_path = os.path.join(settings.STATIC_ROOT, 'images/gojo.jpg')

    p = canvas.Canvas(buffer, pagesize=landscape(A6))

    if last_name != '' or first_name != '':
        p.drawString(0, 250, "Dear " + last_name + " " + first_name)
    else:
        p.drawString(0, 250, "Dear Sir / Madam")

    p.drawImage(img_path, 0, 0, width=480, height=214, mask='auto')

    p.showPage()
    p.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='gratitude.pdf')

def support(request):
    return render(request, 'supports/support.html',)

def donation(request):
    return render(request, 'supports/donation.html',)


# Create your views here.

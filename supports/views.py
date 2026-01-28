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

import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def contact(request):
    return render(request, 'supports/contact.html',)

def donation2(request):
    print("**********1")
    first_name=''
    last_name=''
    email=''
    contribute_fund=''
    if 'first_name' in request.POST:
        first_name = request.POST["first_name"]
    if 'last_name' in request.POST:
        last_name = request.POST["last_name"]
    if 'email' in request.POST:
        email = request.POST["email"]
    if 'contribute_fund' in request.POST:
        contribute_fund = request.POST["contribute_fund"]
 
    if email != '':
        print("**********2")
        buffer2 = io.BytesIO()
        img_path = os.path.join(settings.STATIC_ROOT, 'images/thankyou.jpeg')

        p = canvas.Canvas(buffer2, pagesize=landscape(A6))
        #p.drawString(0, 250, "              Donation Recipt")
        if last_name != '' or first_name != '':
            p.drawString(0, 280, "Dear " + first_name + " " + last_name + ",")
        else:
            p.drawString(0, 280, "Dear Sir / Madam,")

        p.drawString(0, 260, "    We would like to send our sincere thank for your donation. Attached is your")

        p.drawString(0, 240, " receipt for your kind contribution of $" + contribute_fund + ".")

        p.drawString(0, 220, "                                                                                             Best Regards, KYK Foundation")

        p.drawImage(img_path, 0, 0, width=480, height=214, mask='auto')

        p.showPage()
        p.save()

        buffer2.seek(0)

        msg = MIMEMultipart()
        msg['From'] = 'magaystudying@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'fcs receipt'

        # Attach the body of the email
        #msg.attach(MIMEText(body, 'plain'))

        # Attach the PDF
        pdf_attachment = MIMEApplication(buffer2.read(), _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename='receipt.pdf')
        msg.attach(pdf_attachment)

        # Connect to the SMTP server and send the email
        try:
            # Use a secure connection (for Gmail use 'smtp.gmail.com' and port 587 with starttls)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls() # Enable security
            server.login('magaystudying@gmail.com', 'wjcesrppyhuulfkw')
            server.send_message(msg)
            print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error: unable to send email - {e}")
        finally:
            server.quit()

        response_data = {
            'success': True,
            'message': 'Item saved successfully!',
        }

        return JsonResponse(response_data, status=200)

def support(request):
    return render(request, 'supports/support.html',)

def donation(request):
    return render(request, 'supports/donation.html',)
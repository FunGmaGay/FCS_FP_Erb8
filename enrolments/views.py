from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404
from workshops.models import Workshop
from enrolments.models import Enrolment

# Create your views here.
def apply(request, workshop_id):
    if request.user.is_authenticated:
        workshops = get_object_or_404(Workshop, pk=workshop_id)
        context = {"workshop_id": workshop_id, "workshop": workshops.workshop}
        return render(request, 'enrolments/apply.html', context)
    else:
        request.session['enrolment'] = workshop_id
        return render(request, 'accounts/login.html') 
    #return redirect("accounts:dashboard")

def update(request):
    if request.method == 'POST' and request.user.is_authenticated:
        user_id = request.user.id
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        phone = request.POST['phone'] 
        email = request.POST['email']
        workshop_id = request.POST['workshop_id']
        print('user_id=', user_id, ', workshop_id=', workshop_id)
        enrolled = Enrolment.objects.all().filter(workshop_id__id = workshop_id, auth_user_id__id=user_id)
        if enrolled:
            messages.error(request, 'We are sorry to inform you that your application is failed.')
            workshop = get_object_or_404(Workshop, pk = workshop_id)
            context = {"workshop_id": workshop_id, "workshop": workshop.workshop}
            return render(request, 'enrolments/apply.html', context)
        
        auth_user2 = get_object_or_404(User, id=user_id)
        workshop2 = get_object_or_404(Workshop, pk = workshop_id)

        enrolment = Enrolment(
                        auth_user_id=user_id,
                        last_name=last_name,
                        first_name=first_name,
                        gender=gender,
                        email=email,
                        phone=phone,
                        workshop_id=workshop_id
                    )
        enrolment.save()
        
        messages.success(request, 'You have enrolled the course successfully.')
        
        enrolmentList = Enrolment.objects.all().filter(auth_user_id__id = user_id)
        context2 = {"enrolments": enrolmentList}
        
        return render(request, "accounts/dashboard.html", context2)
    else:
        return render(request, 'accounts/login.html') 

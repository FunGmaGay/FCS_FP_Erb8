from django.shortcuts import render

# Create your views here.
def apply(request, workshop_id):
    if request.user.is_authenticated:
        workshop = get_object_or_404(Workshops, pk=workshop_id)
        context = {"workshop_id": workshop_id}
        return render(request, 'enrolments/apply.html', context)
    else:
        return render(request, 'accounts/login.html') 
    #return redirect("accounts:dashboard")

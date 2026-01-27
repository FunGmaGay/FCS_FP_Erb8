# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from enrolments.models import Enrolment

def login(request):
    if request.method == 'POST':
        print("11")
        username = request.POST['username2']
        password = request.POST['password3']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("22")
            print("user.is_authenticated -", user.is_authenticated)
            auth.login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('accounts:dashboard')
        else:
            print("33")
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login') 
    else:
        return render(request, 'accounts/login.html')   

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('pages:index')

def register(request):
    print("test 1")
    if request.method == 'POST':
        print("test 2")
        # Handle registration logic here
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if password == password2:
            print("test 3")
            if User.objects.filter(username=username).exists():
                print("test 4")
                messages.error(request, 'Username already exists!')
                return redirect("accounts:register")
            else:
                print("test 5")
                if User.objects.filter(email=email).exists():
                    print("test 6")
                    messages.error(request, 'Email already exists!')
                    return redirect( "accounts:register")
                else:
                    print("test 7")
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    messages.success(request, 'You have registered successfully and can log in now.')
                    return redirect("accounts:login")
        else: 
            print("test 8")
            messages.error(request, 'Passwords do not match')
            return redirect("accounts:register")
    else: 
        print("test 9")
        return render(request, 'accounts/register.html')

def dashboard(request):
    if request.user.is_authenticated:
        enrol = request.session.get('enrolment', 'mini')
        if enrol == 'mini':
            enrolmentList = Enrolment.objects.all().filter(auth_user_id__id = request.user.id)
            context2 = {"enrolments": enrolmentList}
            return render(request, "accounts/dashboard.html", context2)
        else:
            request.session['enrolment'] = 'mini'
            return redirect("enrolments:apply", str(enrol))
    else:
        return render(request, 'accounts/login.html')


# Create your views here.

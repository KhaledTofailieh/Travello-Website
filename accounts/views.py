from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    return render(request, 'register.html')


def login(request):
    return None


def logout(request):
    return None


def submit_registration(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    user_name = request.POST['username']
    email = request.POST['email']
    password = request.POST['password1']
    confirm = request.POST['password2']

    if password == confirm:
        if User.objects.filter(username=user_name).exists():
            print("username taken!!")
        elif User.objects.filter(email=email).exists():
            print('email taken')
        else:
            user = User.objects.create_user(username=user_name, password=password, email=email,
                                            first_name=first_name, last_name=last_name)
            user.save()
            print("yes created!!")
    else:
        print("password not matched!!")
    return redirect('/travello')



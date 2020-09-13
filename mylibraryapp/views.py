from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Signup
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def index (request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        address=request.POST["address"]
        address2=request.POST["address2"]
        city=request.POST["city"]
        state=request.POST["state"]
        zip=request.POST["zip"]
        acctype=request.POST["acctype"]
        if acctype=="students":
            users = Signup(email=email, address=address, password=password, address2=address2, state=state, city=city,
                           zip=zip, is_student=True, is_teacher=False)
            users.save()
        else:
            users = Signup(email=email, address=address, password=password, address2=address2, state=state, city=city,
                           zip=zip, is_student=False, is_teacher=True)
            users.save()



        user=User.objects.create_user(username=email,password=password,email=email)
        user.save()


        return render(request,"index.html", {"login": "successfully logged in"})
    else:
        return render(request, "index.html")


def login(request):
    if request.method=="POST":
        acctype=request.POST["acctype"]
        email=request.POST["email"]
        password=request.POST["password"]

        sign_up = Signup.objects.get(email=email)
        context = {
            "email": sign_up.email,
            "address": sign_up.address,
            "address2": sign_up.address2,
            "city": sign_up.city,
            "state": sign_up.state,
            "zip": sign_up.zip
        }

        if acctype == "students":
            if True == sign_up.is_student:
                user = auth.authenticate(request=request, username=email, password=password)
                if user is not None:
                    auth.login(request, user)

                    return render(request, "student.html",{"context": context})
                else:
                    return HttpResponse("You are not register as student")
        else:
            if True == sign_up.is_teacher:
                user = auth.authenticate(request=request, username=email, password=password)
                if user is not None:
                    auth.login(request, user)
                    return render(request, "teacher.html",{"context": context})
            else:
                return HttpResponse("You are not register as teacher")
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request=request)
    return redirect("/")


def student(request):
    return render(request,"student.html")


def teacher(request):
    return render(request,"teacher.html")

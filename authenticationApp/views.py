from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate , login , logout
from .forms import CreateUserForm
from .functions import userCreationChecker,checkUserExists,sendEmail
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .decorators import *
# Import Packages For Email
from email.message import EmailMessage
import ssl
import smtplib
# Import Django Messages
from django.contrib import messages



def testView(request):
    return HttpResponse('<h1>Test Page</h1>')



@userAuthenticated
def registerPage(request):
    registerForm = CreateUserForm()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        userEmail = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirmation = request.POST.get('password2')
        processRight = userCreationChecker(firstname , lastname , userEmail ,password, password_confirmation)
        if (processRight):
            try:
                username = firstname + lastname
                new_user = User.objects.create_user(username=username, email = userEmail , password=password)
                user_profile = UserProfile.objects.create(user=new_user,emailAddress= userEmail)
                clientGroup = Group.objects.get(name='clients')
                clientGroup.user_set.add(new_user)
                user_profile.save()
                return HttpResponse("user created successfully")
            except:
                return HttpResponse("User created unsuccessfully")    
        else:
            return HttpResponse("User Not Created Successfully Form Input Not Valid")    
    context = {"form": registerForm}
    return render(request,'registerPage.html',context)



@userAuthenticated
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            return HttpResponse("Authenticated unSuccefully")
    return render(request,'loginPage.html')



@login_required(login_url='loginPage')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')    



def forgetPassword(request):
    if request.method == 'POST':
        usernameSubmitted = request.POST.get('username')
        userExist = checkUserExists(usernameSubmitted)
        if (userExist == True):
            myuser = User.objects.get(username=usernameSubmitted)
            userEmail = (myuser.userprofile.emailAddress)
            messageSent = sendEmail(userEmail,"Email Subject","The Mail Body")
            if (messageSent == True):
                messages.success(request, "Send Message To Email Including Generated Url")
            else:
                messages.error(request, "Error While Sending Email Message!")
        else:
            messages.error(request, "User Not Exist To Send Message To !" )
    return render(request, "forgetPassword.html")


#> Add a decorator to check if the request Token is valid
def changePasswordToken(request):
    return HttpResponse("This View That Take Care of Updating Password After Forgetting Password")



@login_required(login_url='loginPage')
def homePage(request):
    return HttpResponse("Home page lmao")
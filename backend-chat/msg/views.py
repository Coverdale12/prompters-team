from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Request

# for authenticating the user
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    context = {"UserInfo": "Guest"}
    if request.user.is_authenticated:
        context = {"UserInfo": request.user}
    return render(request, "home.html",context)

@csrf_exempt
def register(request):
    if request.method == "POST":
        username =request.POST.get('username')
        email =request.POST.get('email')
        password1 =request.POST.get('password1')
        password2 =request.POST.get('password2')

        if password1 != password2:
            messages.warning(request, "Password do not match")
            return redirect('register')

        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already taken")
            return redirect('register')

        newUser = User.objects.create_user(username,email,password1)
        newUser.save()
        login(request,newUser)
        messages.success(request, "Your account has been created successfully")
        return redirect("home")
    return render(request, "register.html")

@csrf_exempt
def loginuser(request):
    if request.method=="POST":
        username =request.POST.get('username')
        password  =request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            email=user.email
            return redirect("home")
        else:
            messages.warning(request, "Invalid credintials")
            return redirect('login')
    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success( request, "Logged out successfully")
    return redirect ('home')

def findfriends(request):
    UserObjects = User.objects.exclude(username=request.user).order_by().values('username')
    Users = []
    for userObj in UserObjects: Users.append(userObj['username'])

    # requests sent by currently logged in user
    requests_sent = Request.objects.filter(sender = request.user.username)
    requests_recieved = Request.objects.filter(reciever = request.user.username)
    
    # friend list of a user
    friend_list = Request.objects.filter(status = "accepted")
    friend_list = friend_list.filter(sender = request.user.username) | friend_list.filter(reciever = request.user.username)

    context = {
            "users":Users, "requests_sent":requests_sent, "countOfRecivers":requests_sent.count(),
            "requests_recieved":requests_recieved, "countOfSenders" : requests_recieved.count(),
            "friend_list":friend_list,
            "total_friends":friend_list.count(),
    }
    return render(request,"findfriends.html", context)

def user2(request):
    if request.method == "POST":
        username = request.POST.get('username')
    if username == "":
        return redirect("findfriends")
    if User.objects.filter(username = username).exists() == False:
            messages.warning(request, "Invalid username")
            return redirect('findfriends')
    Friends = Request.objects.filter(sender=username, reciever = request.user.username) | Request.objects.filter(reciever=username, sender = request.user.username)
    request_status = ""
    if (len(Friends.values_list('status'))) != 0:
        request_status = list(Friends.values_list('status'))[0][0]
    
    context = {"username": username, "request_status":request_status}
    return render(request,"user.html", context)


def user(request, username):
    if request.method == "POST":
        username = request.POST.get('username')

    if username == request.user.username:
        messages.info(request,"Your profile")
        return redirect("findfriends")
    Friends = Request.objects.filter(sender=username, reciever = request.user.username) | Request.objects.filter(reciever=username, sender = request.user.username) 
    request_status = list(Friends.values_list('status'))[0][0]
    context = {"username": username, "request_status":request_status}
    return render(request,"user.html", context)

def request(request, username):
    print("Sender:",request.user,"Reciver:" ,username)
    newRequest = Request(sorted(request.user.username+username),request.user.username, username, "pending")
    newRequest.save()
    messages.success(request,"Request sent to "+username)
    return redirect("findfriends")

def accept(request, sender):
    print(request.user.username, sender)
    request_tobe_accepted = Request.objects.filter(sender = sender)
    request_tobe_accepted = request_tobe_accepted.filter(reciever = request.user.username)
    if len(request_tobe_accepted) == 0:
        messages.error(request, "No request from "+ sender)
        return redirect("findfriends")
    request_tobe_accepted.update(status = "accepted")
    request_tobe_accepted = Request.objects.filter(reciever = sender)
    request_tobe_accepted = request_tobe_accepted.filter(sender = request.user.username)
    request_tobe_accepted.update(status = "accepted")
    messages.success(request, "Accepted request from "+ sender)
    return redirect("findfriends")

def deletefriend(request, username):
    idOfObj = sorted(request.user.username+username)
    obj = Request.objects.get(id=idOfObj)
    obj.delete()
    messages.success(request, "Deleted friend "+username+" successfully")
    return redirect("findfriends")
    
def reject(request, sender):
    print(request.user.username,"<-",sender)
    request_tobe_rejected = Request.objects.filter(sender = sender)
    request_tobe_rejected = request_tobe_rejected.filter(reciever = request.user.username)
    if len(request_tobe_rejected) == 0:
        messages.error(request, "No request from "+ sender)
        return redirect("findfriends")
    if (list((request_tobe_rejected).values_list('status', flat=True))[0]) == "accepted":
        messages.info(request, sender+" is already in friendlist ")
        return redirect("findfriends")
    request_tobe_rejected.update(status = "rejected")
    request_tobe_rejected = Request.objects.filter(reciever = sender)
    request_tobe_rejected = request_tobe_rejected.filter(sender = request.user.username)
    request_tobe_rejected.update(status = "rejected")
    messages.success(request, "Rejected request from "+ sender)
    return redirect("findfriends")

def message(request):
    messages.info(request, "This feature will be available soon, till then you can connect more people")
    return redirect("findfriends")
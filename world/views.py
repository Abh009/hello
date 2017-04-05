from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from world.models import todo
# Create your views here.

def home(request):
    data = {}

    if request.user == None:
        LogInStatus = True
    else:
        LogInStatus = False
    return render(request,"home2.html",data)

def welcome(request):
    user = request.user
    print(user.username)
    data = {'user':user.username}
    return render(request, "welcome.html", data)

def signup(request):
    data = {}
    if request.method == "POST":
        user = request.POST.get("uname")
        passwrd = request.POST.get("psw")
        u = User.objects.create_user(username=user, password=passwrd)
        if u:
            login(request,u)
            return redirect("/")
    else:
        return render(request,"signup2.html",data)

def login_view(request):
    logout(request)
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("psw")
        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect("/welcome/" )
        else:
            return render(request,"login.html",{"message":"User not found"})
    else:
        data={}
        return render(request,"login.html",data)


def logout_view(request):
    logout(request)
    return redirect("/")
def todo_view(request):
    newItemStatus = False       #new item add status
    if request.method == "POST":
        item = request.POST.get("addText")
        itemNull = False        # to check whether the entered text is null or not
        if item == '':
            data = {'itemNull':itemNull}
            return render(request,"todolist.html",data)
        t = todo.objects.create(text=item)
        newItemStatus = True
        data = {'newItemStatus':newItemStatus}
        return render(request,"todolist.html",data)
    else:
        to = todo.objects.all()
        data = {'todolist':to,'newItemStatus':newItemStatus}
        return render(request,"todolist.html",data)
    
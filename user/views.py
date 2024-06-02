from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ProfileModel
from question.models import QuestionModel
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def sigin_user(request):
    if (request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]

        if username=="" or password=="":
            return redirect(to="/user/signin")
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect("/")
        else: return redirect(to="/user/signin")
    else: return render(request=request, template_name="signin.html")


async def sigup_user(request):
    if (request.method == "POST"):
        name = request.POST["name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        pic = request.POST["pic"]

        if name=="" or email=="" or username=="" or password=="":
            return redirect(to="/user/signup")
        
        try:
            newUser = await User.objects.acreate(username=username, email=email)
            newUser.set_password(password)
            await newUser.asave()

            newProf = await ProfileModel.objects.acreate(account=newUser, name=name)
            if pic:
                newProf.pic = pic
            
            await newProf.asave()
            return redirect(to="/user/signin")
        except Exception as e:
            print(e)
            return redirect(to="/user/signup")
    else: return render(request=request, template_name="signup.html")

def logout_user(request):
    logout(request=request)
    return redirect("/")

def user_profile(request):
    if request.user.is_authenticated:
        acc =User.objects.get(id=request.user.id)
        pro =ProfileModel.objects.get(account=request.user)
        ques=QuestionModel.objects.filter(creator = acc)
        return render(request=request, template_name="profile.html", context={"profile":pro, "account":acc, "questions": ques})
    else: return redirect("/user/signin")
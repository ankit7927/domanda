from django.shortcuts import render, redirect
from .models import QuestionModel, AnswerModel, TagModel
from user.models import ProfileModel
# Create your views here.

def new_question(request):
    if request.method == "POST":
        user = request.user
        if user.is_authenticated:
            title = request.POST["title"]
            content = request.POST["content"]
            tags = request.POST["tags"]
            if content == "":
                return redirect(to="/question/new")
            
            new_q = QuestionModel.objects.create(title=title, content=content, creator=user)
            new_q.save()
            tags = tags.split(",")
            for tag in tags:
                t = TagModel.objects.get_or_create(name=(tag).strip().lower())
                new_q.tags.add(t[0])
            new_q.save()
            return redirect(to="/question/get/"+new_q.slug)
        else: return redirect(to="/user/signin")
    else: return render(request=request, template_name="new.html")    


def get_questions(request, slug=None):
    if slug is not None:
        question = QuestionModel.objects.get(slug=slug)
        answers = AnswerModel.objects.filter(question=question)
        return render(request=request, template_name="question.html", context={"question":question, "answers":answers})
    
    else:
        questions = QuestionModel.objects.values("title", "created", "slug").all()[:15]
        return render(request=request, template_name="questions.html", context={"questions": questions})


def edit_question(request, questionId):
    user = request.user
    if user.is_authenticated: 
        if request.method=="POST":
            title = request.POST["title"]
            content = request.POST["content"]
            QuestionModel.objects.filter(id=questionId).update(title=title, content=content)
            return redirect(to=request.GET.get("success"))
        else: 
            question = QuestionModel.objects.get(id=questionId)
            return render(request=request, template_name="new.html", context={"question":question, "success":request.GET.get("success")})
    else: return redirect("/user/signin")

def delete_question(request, questionId):
    user = request.user
    if user.is_authenticated: 
        QuestionModel.objects.filter(id=questionId).delete()
        return redirect("/question/get") 
    else: return redirect("/user/signin")


def new_answer(request, questionId):
    user = request.user
    if user.is_authenticated:
        ansdata = request.POST["answer"]
        if ansdata=="":
            return redirect(to=request.GET.get("success"))
        AnswerModel.objects.create(content=ansdata, creator=user, question=QuestionModel.objects.get(id=questionId))
        return redirect(to=request.GET.get("success"))
    else: return redirect("/user/signin")

def delete_answer(request, answerId):
    user = request.user
    if user.is_authenticated:
        AnswerModel.objects.filter(id=answerId).delete()
        return redirect(to=request.GET.get("success"))
    else: return redirect("/user/signin")

def like_dislike_question(request, questionId):
    user = request.user
    if user.is_authenticated: 
        question = QuestionModel.objects.get(id=questionId)
        user_profile = ProfileModel.objects.get(account=user)

        if user_profile.liked_questions.filter(id=questionId).exists():
            user_profile.liked_questions.filter(id=questionId).delete()
            question.likes -= 1

        else:
            user_profile.liked_questions.add(question)
            question.likes +=1
        question.save()

        return redirect(to=request.GET.get("success"))
    else: return redirect("/user/signin")
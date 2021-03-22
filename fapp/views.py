from django.shortcuts import render,redirect
from .models import addproject, comment_project, donnate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import  myForm, myModelForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def addproject_form(request):
    return render(request,'addproject.html',{})

def addproject_database(request):
    obj=addproject()
    id=request.user.id
    tittle= request.POST['tit']
    details = request.POST['det']
    cateogry = request.POST['cat']
    target = request.POST['target']
    img = request.POST['img']
    sdate = request.POST['sdate']
    enddate = request.POST['enddate']
    obj.tittle=tittle
    obj.details=details
    obj.category=cateogry
    obj.total_target=target
    obj.uploadimg=img
    obj.startdate=sdate
    obj.edndate=enddate
    obj.id_user=id
    obj.save()
    return redirect('homepage')

def addproject_table(request):
    i=0
    list2=[]
    obj2 = addproject.objects.all()
    list=addproject.objects.order_by('-startdate')
    while(i<5):
        list2.append(list[i])
        i=i+1
    return render(request, 'home.html', {'data': obj2,'list':list2})


#def register_form(request):
 #   return render(request,'adduser.html',{})
def registerAuth(request):
    if request.method == 'POST':
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            pass1 = form.cleaned_data['password']
            user = User.objects.create_user(username=fname,last_name=lname,password=pass1)
            user.save()

            # redirect to a new URL:
            return HttpResponse('user rigestred')
    else:
       form = myForm()
    return render(request, 'adduser.html', {'form': form})
def home_view(request):
    return render(request, 'home.html')

def loginAuth(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = myModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fname = form.cleaned_data['username']
            pass1 = form.cleaned_data['password']
            # redirect to a new URL:Authinticate
            user = authenticate(username=fname,password=pass1)
            if user is not None:
                login(request, user)
                return redirect('homepage')
                #logout(request)
                #return HttpResponse('/login found/')
            else:
                return HttpResponse('/not found/')
    else:
        form = myModelForm()
        return render (request, 'login.html', {'form': form})

def profile_user(request):
    projects=addproject.objects.all().filter(id_user=request.user.id)
    return render(request,'profile.html',{'data':projects})

def comment(request,id):
    obj=comment_project.objects.all().filter(project_id=id)
    return render(request,'comment.html',{'data':obj,'id':id})
def add_comment(request,id):
    obj=comment_project()
    comment =request.POST['com']
    obj.comment=comment
    obj.project_id=id
    obj.save()
    return redirect('homepage')

def donate_form(request,id):
    return render(request,'donnate.html',{'id':id})
def add_donnate(request,id):
    name=request.POST['name']
    amount=request.POST['amount']
    obj=donnate()
    obj.name=name
    obj.amount=amount
    obj.project_id=id
    obj.save()
    return redirect('homepage')

def donateprojects(request,id):
    donntes=donnate.objects.all().filter(project_id=id)
    total=0
    for i in donntes:
        total=total+i.amount
    return render(request,'donnate_projects.html',{'id':id,'data':donntes,'total':total})

def remove_projects(request,id,totaldonnates):
    objproject=addproject.objects.filter(id=id)
    objcomment = comment_project.objects.all().filter(project_id=id)
    objdonnate = donnate.objects.all().filter(project_id=id)
    d=.25*objproject.total_target
    if (d<totaldonnates):
        objproject.delete()
        objcomment.delete()
        objdonnate.delete()
        return redirect('profile')
    return ("can,t delete project")
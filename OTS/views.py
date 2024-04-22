from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from OTS.models import *


def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())
def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res
def candidateRegistration(request):
    if request.method == "POST":
        username=request.POST['username']
        # check if the user is already exists
        if(len(Candidates.objects.filter(username=username))):
            userStatus=1
        else:
            candidate=Candidates()
            candidate.username=username
            candidate.password=request.POST['password']
            candidate.name=request.POST['name']
            candidate.save()
            userStatus=2

    else:
        userStatus=3 #Request method is not POST
    context={
        'userStatus':userStatus
    }
    res=render(request,'registration.html',context)
    return res

def loginView(request):
     if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        candidate=Candidates.objects.filter(username=username,password=password)

        if len(candidate)==0:
            loginError="Invalid Username or Password"
            res=render(request,'login.html',{'loginError':loginError})
        else:
            # Login sucess
            request.session['username']=candidate[0].username
            request.session['name']=candidate[0].name
          #  return redirect ('candidateHome')
            res=HttpResponseRedirect('home')
            return res
     else:
        res= render(request,'login.html')
        return res
     
def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login.html")
    else:
        res=render(request,'home.html')
        return res

def testPaper(request):
    pass
def calculateTestResult(request):
    pass
def testResultHistory(request):
    pass
def showTestResult(request):
    pass
def logoutView(request):
    pass


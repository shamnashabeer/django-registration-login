from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Contact
from .models import Registration

# Create your views here.
def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render())
def contact(request):
    if request.method =='POST':
        contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_msg=request.POST['contact_msg']

        contact= Contact(contact_name=contact_name,
                        contact_email=contact_email,
                        contact_msg=contact_msg)
        contact.save()
    template=loader.get_template("contact.html")
    return HttpResponse(template.render({},request))
def index(request):
    template=loader.get_template("home.html")
    return HttpResponse(template.render())
def style(request):
     template=loader.get_template("style.html")
     return HttpResponse(template.render())
def new(request):
     template=loader.get_template("new.html")
     return HttpResponse(template.render())


def registration(request):
    if 'user' in request.session:
        return HttpResponseRedirect("account")

    if request.method =='POST':
       registration_name=request.POST['registration_name']
       registration_email=request.POST['registration_email']
       registration_num=request.POST['registration_num']
       registration_use=request.POST['registration_use']
       registration_pass=request.POST['registration_pass']
       

       registration=Registration(registration_name=registration_name,
                registration_email=registration_email,
                registration_num=registration_num,
                registration_use=registration_use,
                registration_pass=registration_pass)
       registration.save()

    template=loader.get_template("registration.html")
    return HttpResponse(template.render({},request))

def login(request):
    if 'user' in request.session:
        return HttpResponseRedirect("account")
    
    if request.method =='POST':
        login_user=request.POST['login_user']
        login_word=request.POST['login_word']

        login = Registration.objects.filter(
            registration_use=login_user,
            registration_pass=login_word).values()
        if(login):
            request.session['user'] = login_user
            return HttpResponseRedirect("account")
       
    template=loader.get_template("login.html")
    return HttpResponse(template.render({},request))


def account(request):
    if 'user' in request.session:
        template =loader.get_template("account.html")
        return HttpResponse(template.render())
    else:
        return HttpResponseRedirect("login")

def logout(request):
    del  request.session['user']
    return HttpResponseRedirect("login")  
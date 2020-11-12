from django.shortcuts import render
from .models import Seminar_Webinar,Training,Job,Industrial_Trainging,Workshop,Internship,Services,PortFollio

def home(request):
    data = {
        "Services":Services.objects.all(),
        "ports":PortFollio.objects.all()
    }
    return render(request,"index.html",data)

def seminar(request):
    data = {
        "seminars":Seminar_Webinar.objects.all()
    }
    return render(request,"seminar.html",data)

def training(request):
    data = {
        "trainings":Training.objects.all()
    }
    return render(request,"training.html",data)
def job(request):
    data = {
        "jobs":Job.objects.all()
    }
    return render(request,"job.html",data)

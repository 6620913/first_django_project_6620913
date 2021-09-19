from django.shortcuts import render
from django.http import HttpResponse
from .models import courses

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'NEERAJ'})

def add(request):
    val1 = int(request.POST["fname"])
    val2 = int(request.POST["lname"])
    res = val1+val2;
    return render(request,'result.html',{'result': res})

def index(request):


    dests=courses.objects.all()
    return render(request,'index.html',{'dests':dests})
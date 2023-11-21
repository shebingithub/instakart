from django.shortcuts import render
from django.http import HttpResponse


from.models import Department



def index(request):
    return render(request,'index.html')

def about(request):
    dict_dept={
        'dept':Department.objects.all()
    }

    return render(request,'about.html',dict_dept)



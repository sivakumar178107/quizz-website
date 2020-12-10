from django.shortcuts import render
from django.http import HttpResponse
from onlineexam.models import exam
# Create your views here.
def home(request):
    results=exam.objects.all()
    return render(request,"index.html",{'exam':results})

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.models import Place
from.models import team
# Create your views here.






def demo(request):
    obj=Place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})

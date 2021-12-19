from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE



def button(request):
    return render(request,'home.html')

def output(request):
    data = requests.get("https://reqres.in/api/users")
    print(data.text)
    data = data.text
    return render(request,'home.html',{'data':data})

def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable,'//d//Python//Projects//APDCL_Project_2//pr2',inp],shell=False,stdout=PIPE)
    print(out)

    return render(request,'home.html',{'data1':out})
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calc(request):
    return render(request,'calc.html')
def add(request):
    n1 = int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    res = n1 + n2
    return render(request,'result.html',{"result": res})


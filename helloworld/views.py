from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_world(request):
    return render(request, 'home.html', {"name": "خالد"})


def add_numbers(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    result = int(num1) + int(num2)
    return render(request, 'result.html', {"result": result})

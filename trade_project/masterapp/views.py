from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    if request.POST:

        if request.POST['value1']!="" and request.POST['value2']!="":
            sum = int(request.POST['value1']) + int(request.POST['value2'])
            return render(request, 'masterapp/index.html', context = {'sum': sum})

        else:
            return render(request, 'masterapp/index.html', context= {'error': "You didn't enter both the values."})

    else:
        return render(request, 'masterapp/index.html')


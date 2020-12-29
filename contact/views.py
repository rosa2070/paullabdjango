from django.shortcuts import render

def contactindex(request):
    return render(request, 'contact/index.html')

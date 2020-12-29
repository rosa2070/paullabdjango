from django.shortcuts import render

def aboutindex(request):
    return render(request, 'about/index.html')

from django.shortcuts import render

def noticeindex(request):
    return render(request, 'notice/index.html')

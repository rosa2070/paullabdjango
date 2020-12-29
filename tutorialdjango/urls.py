from django.contrib import admin
from django.urls import path
from main.views import mainindex
from about.views import aboutindex
from notice.views import noticeindex
from contact.views import contactindex

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainindex),
    path('about/', aboutindex),
    path('notice/', noticeindex),
    path('contanct/', contactindex),
]

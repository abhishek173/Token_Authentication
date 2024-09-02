from django.contrib import admin
from django.urls import path
from login.views import StudentApi,LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',StudentApi.as_view()),
    path('login/',LoginAPI.as_view()),
]

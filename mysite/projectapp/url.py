from django.contrib import admin
from django.urls import path, include
from projectapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]
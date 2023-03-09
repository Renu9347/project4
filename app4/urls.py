from django.urls import path,include
import app3,app4
urlpatterns=[
    path('app3/',include('app3.views')),
    path('app4/',include('app4.views')),
]
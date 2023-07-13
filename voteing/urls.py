
from django.urls import path, include
from voteing import views

urlpatterns = [
    path('', views.index.as_view(), name='voteingindex'),
    #path('', views.index, name='main-view'),
]

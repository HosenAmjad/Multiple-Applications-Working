

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class index(View):
    def get(self, request):
        return render(request, 'base.html')

class login(View):
    def get(self, request):
        return render(request, 'login.html')

class signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(slef, request):
        return render(request, 'login.html')

class terms(View):
    def get(self, request):
        return render(request, 'terms.html')

class helps(View):
    def get(self, request):
        return render(request, 'helps.html')

class privace(View):
    def get(self, request):
        return render(request, 'privace.html')
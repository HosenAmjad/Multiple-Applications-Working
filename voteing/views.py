

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class index(View):
    def get(self, request):
        return render(request, 'voteingapp/index.html')




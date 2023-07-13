

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from .models.questions import userQuestions
from .models.choices import userChoice


class pollindex(View):
    @method_decorator(login_required)
    def get(self, request):
        latest_question_list = userQuestions.objects.order_by('-register_on')[:5]
        output = ', '.join([q.question_text for q in latest_question_list])
        context = {
            'latest_question_list':latest_question_list
        }
        return render(request, 'pollapp/index.html', context)
    
    @method_decorator(login_required)
    def post(self, resquest):
        pass
    

class details(View):
    @method_decorator(login_required)
    def get(self, request, id):
        ques_choice = get_object_or_404(userQuestions, pk=id)
        context={
            'uqchoice':ques_choice,
        }
        return render(request, 'pollapp/details.html', context)
    
    @method_decorator(login_required)
    def post(self, request, id):
        ques_choice = get_object_or_404(userQuestions, pk=id)
        try:
            selected_choice = ques_choice.userchoice_set.get(pk = request.POST['voteing'])
        except (KeyError, userChoice.DoesNotExist):
            return redirect('pollindex')
        else:
            selected_choice.votes += 1
            selected_choice.save()
            context = {
            }
            return redirect ('pollindex')




class previouspost(View):
    @method_decorator(login_required)
    def get(self, request, id):
        try:
            ques_choice = get_object_or_404(userQuestions, pk=id-1)
            context={
                'uqchoice':ques_choice,
            }
            return render(request, 'pollapp/details.html', context)
            
        except:
            ques_choice = get_object_or_404(userQuestions, pk=id)
            context={
                'uqchoice':ques_choice,
            }
            return render(request, 'pollapp/details.html', context)
    
    @method_decorator(login_required)
    def post(self, request, id):
        ques_choice = get_object_or_404(userQuestions, pk=id-1)
        try:
            selected_choice = ques_choice.userchoice_set.get(pk = request.POST['voteing'])
        except:
            return redirect('pollindex')
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponse(selected_choice)
        


class nextpost(View):
    @method_decorator(login_required)
    def get(self, request, id):
        try:
            ques_choice = get_object_or_404(userQuestions, pk=id+1)
            context={
                'uqchoice':ques_choice,
            }
            return render(request, 'pollapp/details.html', context)
            
        except:
            ques_choice = get_object_or_404(userQuestions, pk=id)
            context={
                'uqchoice':ques_choice,
            }
            return render(request, 'pollapp/details.html', context)
    
    @method_decorator(login_required)
    def post(self, request, id):
        ques_choice = get_object_or_404(userQuestions, pk=id+1)
        try:
            selected_choice = ques_choice.userchoice_set.get(pk = request.POST['voteing'])
        except:
            return redirect('pollindex')
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponse(selected_choice)
        
        

        


class pollsearch(View):
    @method_decorator(login_required)
    def get(self, request):
        search = request.GET.get('searchpoll')
        q = userQuestions.objects.filter(question_text__icontains=search)
        context={
            'uqchoice':q,
        }
        return render(request, 'pollapp/search.html', context)
    
    @method_decorator(login_required)
    def post(self, request):
        pass
        
        




class results(View):
    @method_decorator(login_required)
    def get(self, request, id):
        ques_choice = get_object_or_404(userQuestions, pk=id)
        context={
            'uqchoice':ques_choice,
        }
        return render(request, 'pollapp/results.html', context)
    
class resultsall(View):
    @method_decorator(login_required)
    def get(self, request):
        choices = userChoice.objects.all()
        context={
            'choices':choices,
        }
        return render(request, 'pollapp/resultsall.html', context)

class searchresultsall(View):
    @method_decorator(login_required)
    def get(self, request):
        search = request.GET.get('searchvote')
        print(search)
        q = userChoice.objects.filter(choice__icontains=search)
        context={
            'choices':q,
        }
        return render(request, 'pollapp/resultsall.html', context)

    
class create(View):
    @method_decorator(login_required)
    def get(self, request):
        questions = userQuestions.objects.all()
        context={
            'queschoices':questions,
        }
        return render(request, 'pollapp/create.html', context)

    def post(self, request):
        quesid = request.POST['selectques']
        addvote = request.POST['voteadd']
        print(quesid)
        print(addvote)
        newChoice = userChoice.objects.create(question=quesid, choice=addvote)
        newChoice.save()
        return redirect('pollcreate')


            


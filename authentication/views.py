

# Create your views here.
from base64 import urlsafe_b64decode
from email.message import EmailMessage
from django.core.mail import EmailMessage, send_mail
from tokenize import generate_tokens
from .tokens import account_activation_token
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
# from django.utils.encoding import force_text
from django.utils.encoding import force_str

from applications import settings
from .models.signup import signupUser
import re


class index(View):
    def get(self, request):
        return render(request, 'index.html')



class userlogin(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('/')
    
    
    def post(self, request):
        usernames = request.POST['useremail']
        passwords = request.POST['userpassword']
        print(usernames, passwords)
        user = authenticate(request, username=usernames, password=passwords)
        if user  is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('userlogin')

class userlogout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class signup(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'signup.html')
        else:
            return redirect('/')
    
    def post(slef, request):
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        repassword = request.POST['repassword']
        #checkBox = request.POST['checkbox']

        gatname = firstName+""+lastName
        joinname = ''.join(gatname)
        replacedot = joinname.replace('.', '')
        cleandata = re.sub(r"\s+", "", replacedot)
        fullName = cleandata


        print(firstName, lastName, email)
        Error_Message=None

        if not firstName:
            Error_Message = "First Name must is Required !!"
        elif len(firstName) < 4:
            Error_Message = "First Name must be at least 4 characters long or more !!"
        elif (not lastName):
            Error_Message = "Last Name must is Required !!"
        elif len(lastName) < 4:
            Error_Message = "Last Name must be at least 4 characters long or more !!"
        elif (not email):
            Error_Message = "Must is Required e-mail address !!"
        elif (not mobile):
            Error_Message = "Must is Required valid Mobile Number !!"
        elif not password:
            Error_Message = "Password must is Required !!"
        elif len(password) < 6:
            Error_Message = "Password must be at least 6 characters and number long or more !!"
        elif (not repassword):
            Error_Message = "Repassword must is Required !!"
        elif len(repassword) < 6:
            Error_Message = "Repassword must be at least 6 characters and number long or more !!"
        print(Error_Message)

        value = {'firstName':firstName, 'lastName':lastName, 'email':email, 'mobile':mobile}

        if not Error_Message:
            if password==repassword:
                if signupUser.objects.filter(email=email).exists():
                    Error_Message = "Email is Allready Registered !! "+email
                    context = {
                        'Error_Message':Error_Message, 'value':value
                    }
                    return render(request, 'signup.html', context)
                elif signupUser.objects.filter(mobile=mobile).exists():
                    Error_Message = "Number is Allready Registered !! "+mobile
                    context = {
                        'Error_Message':Error_Message, 'value':value
                    }
                    return render(request, 'signup.html', context)
                else:
                    newUser = signupUser(firstName=firstName, lastName=lastName, userName=fullName, email=email, mobile=mobile, password=make_password(repassword))
                    newUser.save()
                    Admin_user = User.objects.create(first_name=firstName, last_name=lastName, username=fullName, email=email, password=make_password(password), is_staff =True)
                    Admin_user.is_active = False
                    Admin_user.save()
                    SuccessMessage = "Success full message user create "+fullName

                    #CONFIRM MESSAGE
                    confirm_message = "Confirmation Message"

                    #WELCOME MESSAGE
                    subject = "Welcome to Nexus Technologies Django login!!"
                    message = "Hello " + Admin_user.first_name + "!!\n" + "Welcome to nexus!! \nThank you for visiting our website \nwe have also sent you confirmation email, please confirm your email address in order to activate your account.\n\nThanking you\nMd. Amjad Hosen"
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [Admin_user.email]
                    send_mail(subject, message, from_email, to_list, fail_silently=True)

                    # Email Confiramations Message
                    current_site = get_current_site(request)
                    email_subject = "confirm your email @ NEXUS - Django Login!!"
                    messageCon = render_to_string('email_confimation.html',{
                        'name': Admin_user.first_name,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(Admin_user.pk)),
                        'token': account_activation_token.make_token(Admin_user),
                    })
                    email = EmailMessage(
                        email_subject,
                        messageCon,
                        settings.EMAIL_HOST_USER,
                        [Admin_user.email]
                    )
                    email.fail_silently = True
                    email.send()
                    return  redirect('userlogin')
            else:
                Error_Message = "Your Password didn't Meathch !! "
                context = {
                    'Error_Message':Error_Message, 'value':value
                }
                return render(request, 'signup.html', context)
        else:
            Error_Message = Error_Message
            context = {
                'Error_Message':Error_Message, 'value':value
            }
            return render(request, 'signup.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        Admin_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        Admin_user = None
    
    if Admin_user is not None and account_activation_token.check_token(Admin_user, token):
        Admin_user.is_active = True
        Admin_user.save()
        login(request, Admin_user)
        return redirect('index')
    else:
        return render(request, 'activation_failed.html')



        
class deshboards(View):
    @method_decorator(login_required)
    def get(self, request):
        signinfo = signupUser.objects.all()
        context={
            'signinfo' : signinfo
        }
        return render(request, 'profile/index.html', context)



class terms(View):
    def get(self, request):
        return render(request, 'terms.html')

class helps(View):
    def get(self, request):
        return render(request, 'helps.html')

class privace(View):
    def get(self, request):
        return render(request, 'privace.html')
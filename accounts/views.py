from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    print(type(send_mail))
    send_mail(
        'Your login link for Superlists',
        'Use this link to log in',
        'noreply@superlists',
        [email]
    )

    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    return redirect('/')
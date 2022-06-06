from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        send_mail(
            'testing',content,settings.EMAIL_HOST_USER,[to]
        )
        return render(request,'email.html',{ 'title': 'Send-Email'})


    else:
        return render(request,'email.html',{ 'title': 'Send-Email'})
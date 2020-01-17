from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return render(request, 'login.html', {})


def verifyPage(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')
        from .models import AccountModel as AM
        try:
            AM.objects.get(user=u)
            return HttpResponse('Login Sucess')
        except:
            a = AM()
            a.user = u
            a.pwd = p
            a.save()
            return HttpResponse('Account Created')

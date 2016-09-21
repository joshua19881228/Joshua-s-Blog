from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def account_login_view(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/topic_ALL_list/')
    else:
        return HttpResponseRedirect('/topic_ALL_list/')


def account_logout_view(request):
    logout(request)
    return HttpResponseRedirect('/topic_ALL_list/')

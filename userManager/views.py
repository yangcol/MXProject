#encoding:utf-8
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required(login_url="/login/")
def home(request):
    return render_to_response("home.html")
    #return HttpResponse('Welcome, <a target="_blank" href="/logout/">logout</a>')


def my_view(request):
    if not (request.user.is_authenticated() and request.user.has_perm('polls.can_vote')):
        return HttpResponse("You can't vote in this poll.")


def show_users(request):
    return render_to_response('user.html')
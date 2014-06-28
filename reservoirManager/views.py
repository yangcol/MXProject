# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect


@user_passes_test(lambda u: u.has_perm('polls.can_vote'), login_url='/login/')
def home(request):
    assert(request.method == 'GET')
    #return render_to_response("home.html", {'navigate':[]})
    if not(request.user.is_authenticated() and request.user.has_perm("polls.can_vote")):
        return HttpResponse("You can vote in this poll")
    else:
        return HttpResponse("You can't")
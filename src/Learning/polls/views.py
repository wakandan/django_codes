# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from django.template.context import RequestContext
from models import Poll, Choice


#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
##    t = loader.get_template('index.html')
##    c = Context({
##        'latest_poll_list': latest_poll_list
##    })    
##    return HttpResponse(t.render(c))
#    return render_to_response('index.html',
#                              {'latest_poll_list':latest_poll_list})
#def detail(request, poll_id):
##    try:
##        poll = Poll.objects.get(pk=poll_id)
##    except Poll.DoesNotExist:    
##        raise Http404
##    return render_to_response('detail.html',
##                              {'poll':poll})
#    poll = get_object_or_404(Poll, pk=poll_id)
#    return render_to_response('detail.html',
#                              {'poll':poll},
#                              #this is for CSRF token 
#                              context_instance=RequestContext(request))
#def results(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    return render_to_response('results.html',
#                              {'poll':p})
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the voting form
        return render_to_response('detail.html',
                                  {'object':poll,
                                   'error_msg':'You did not select a choice'},
                                   context_instance=RequestContext(request))
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results',
                                            args=(poll.id,)))


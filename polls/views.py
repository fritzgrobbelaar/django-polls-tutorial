from django.shortcuts import render,get_object_or_404
#from .models import Question
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.utils import timezone
from .models import Question,Choice
from django.urls import reverse
from django.views import generic

def fritz(request):
        return HttpResponse("Hello, world. You're at the polls index - Fritz: "+str(datetime.datetime.now()))

# Create your views here.

# def detail(request, question_id):
#     latest_question = get_object_or_404(Question,pk=question_id)
#     #choices = get_object_or_404(Choice,pk=)
#     #template = loader.get_template("polls/detail.html")
#     context = {'question': latest_question}
#     return render(request,'polls/detail.html',context)
#  #   return HttpResponse(template.render(context,request))

#    return HttpResponse("You're looking at question %s." %question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class Resultsview(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." %question_id)
    question = get_object_or_404(Question,pk=question_id)
    print("page loaded increased")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("choice selecte")
    except (KeyError, Choice.DoesNotExist):
        print("choice selected NOT")
        return render (request,'polls/detail.html', {'question':question, 'error_message': "You didn't select a choice."})
    else:
        print("Vote increased on the second place")
        selected_choice.votes += 1
        selected_choice.save()
        print('reversed result:',reverse('polls:results', args=(question.id,)))
        #return HttpResponseRedirect('../../'+str(question.id)+"/results")

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     #output = ", ".join([q.question_text for q in latest_question_list])
#     template = loader.get_template("polls/index.html")
#     context = {'latest_question_list': latest_question_list,}
#     return HttpResponse(template.render(context,request))
from django.shortcuts import render,get_object_or_404
#from .models import Question
from django.template import loader
from django.http import HttpResponse
import datetime
from polls.models import Question

def fritz(request):
        return HttpResponse("Hello, world. You're at the polls index - Fritz: "+str(datetime.datetime.now()))

# Create your views here.

def detail(request, question_id):
    latest_question = get_object_or_404(Question,pk=question_id)
    template = loader.get_template("polls/detail.html")
    context = {'question': latest_question}
    return HttpResponse(template.render(context,request))

#    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context,request))
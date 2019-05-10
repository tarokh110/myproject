
from django.shortcuts import render
from django.http import HttpResponse
from zmq.sugar import context

from .models import Question
# Create your views here.



def index(request):
    return render(request, 'myapp/index.html')


def about(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }

    return render(request, 'myapp/about.html', {questions: 'questions'})


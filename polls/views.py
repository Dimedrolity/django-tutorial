# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]

    return render(request, 'polls/index.html', context={
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', context={
        'question': question
    })


def results(request, question_id):
    return HttpResponse(f' results of q = {question_id}')


def vote(request, question_id):
    return HttpResponse(f'voting for q = {question_id}')

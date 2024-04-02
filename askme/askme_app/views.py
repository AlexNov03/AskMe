from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator



def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    if (not page_num or int(page_num) < 1 or int(page_num) > paginator.num_pages):
        page_num = 1
    return paginator.page(page_num)


def index(request):
    return render(request, 'index.html', {'questions': paginate(models.QUESTIONS, request)})


def hot(request):
    reversed_questions = models.QUESTIONS[::-1]
    context = {'questions' : paginate(reversed_questions , request, per_page=3)}
    return render(request, 'hot.html', context)


def question(request, question_id):
    context = {'question' : models.QUESTIONS[question_id], 
               'correct_card_questions': paginate(models.CORRECT_CARD_QUESTIONS, request, per_page=2)}
    return render(request, 'question.html', context)


def tag(request, tag_str):
    context = {'tag' : tag_str, 
               'questions' : paginate(models.QUESTIONS, request, per_page=3)}
    return render(request, 'tag.html', context)

def login(request):
    return render(request, 'login.html')

def ask(request):
    return render(request, 'ask.html')

def signup(request):
    return render(request, 'signup.html')

def settings(request):
    return render(request, 'settings.html')











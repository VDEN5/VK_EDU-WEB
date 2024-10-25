from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    return render(request,'main/index.html')
def about(request):
    return render(request,'main/about.html')
def tag(request,num):
    tag=num
    questions = []
    for i in range(20):
        questions.append({"author": f"Автор {i + 1}", "tags": [tag, i * 2],
                          "quest_data": "Текст статьи или поста. Здесь может быть много информации о чем-то интересном.",
                          "nums_of_answers": i * 3})
    paginator = Paginator(questions, 10)  # Пагинация по 5 вопросов на страницу
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context1 = {'questions': page.object_list,
                'paginator': paginator,
                'page': page,
                'tag': tag}
    return render(request, 'main/tagquest.html', context=context1)
def question(request,num):
    answers = []
    for i in range(5):
        answers.append({"author": f"Автор {i + 1}", "tags": [i, i * 2],
                    "ans_data": "Текст ответа или поста. Здесь может быть много информации о чем-то интересном."})
    return render(request,'main/question.html', context={'num': num,'answers':answers,'ask':'data ask'})
def ask(request):
    return render(request,'main/ask.html')
def login(request):
    return render(request,'main/login.html')
def signup(request):
    return render(request,'main/signup.html')
def page(request,num):
    return render(request,'main/tagquest.html', context={'num': num})
def hot(request):
    questions = []
    for i in range(20):
        questions.append({"author": f"Автор {i + 1}", "tags": [i, i * 2],
                          "quest_data": "Текст статьи или поста. Здесь может быть много информации о чем-то интересном.",
                          "nums_of_answers": i * 3})
    paginator = Paginator(questions, 5)  # Пагинация по 5 вопросов на страницу
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context1 = {'questions': page.object_list,
                'paginator': paginator,
                'page': page, }
    return render(request, 'main/hot.html', context=context1)
def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return {
        'page': page,
        'paginator': paginator,
    }
def asa(request):
    questions=[]
    for i in range(50):
        questions.append({"author":f"Автор {i+1}","tags":[i,i*2],
                    "quest_data":"Текст статьи или поста. Здесь может быть много информации о чем-то интересном.",
                    "nums_of_answers":i*3})
    paginator = Paginator(questions, 10)  # Пагинация по 10 вопросов на страницу
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context1 = {'questions': page.object_list,
                'paginator': paginator,
                'page': page, }
    return render(request, 'main/questions_list.html', context=context1)
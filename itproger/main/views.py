from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,paginate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def about(request):
    return render(request,'main/about.html')
def tag(request,num):
    tag=num
    questions = []
    for i in range(20):
        questions.append({"author": f"Автор {i + 1}", "tags": [tag, i * 2],
                          "quest_data": "Текст статьи или поста. Здесь может быть много информации о чем-то интересном.",
                          "nums_of_answers": i * 3})
    #paginator = Paginator(questions, 10)  # Пагинация по 5 вопросов на страницу
    page = paginate(questions, request, per_page=10)
    page_number = request.GET.get('page')
    context1 = {'questions': page.object_list,
                'paginator': page.paginator,
                'page': page,
                'tag': tag}
    return render(request, 'main/tagquest.html', context=context1)
def question(request,num):
    answers = []
    for i in range(20):
        answers.append({"author": f"Автор {i + 1}", "tags": [i, i * 2],
                    "ans_data": "Текст ответа или поста. Здесь может быть много информации о чем-то интересном."})
    page_number = request.GET.get('page')
    page = paginate(answers, request, per_page=10)
    return render(request,'main/question.html', context={'num': num,'answers':page.object_list,'ask':'data ask',
                                                         'paginator':page.paginator,'page':page})
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
    page = paginate(questions, request, per_page=10)
    context1 = {'questions': page.object_list,
                'paginator': page.paginator,
                'page': page, }
    return render(request, 'main/hot.html', context=context1)

def asa(request):
    questions = []
    for i in range(50):
        questions.append({"author": f"Автор {i+1}", "tags": [i, i*2],
                    "quest_data": "Текст статьи или поста. Здесь может быть много информации о чем-то интересном.",
                    "nums_of_answers": i*3})

    # Используем функцию paginate для пагинации
    page = paginate(questions, request, per_page=10)

    context1 = {'questions': page.object_list,
                'paginator': page.paginator,  # Доступ к paginator через page.paginator
                'page': page, }

    return render(request, 'main/questions_list.html', context=context1)
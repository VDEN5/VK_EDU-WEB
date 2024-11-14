from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Quests, QuestionLike,Tags1,QuestsManager
from .utils import paginate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def about(request):
    return render(request,'main/about.html')
def tag(request,num):
    tag=num
    questions = []
    qw=QuestsManager.get_best()
    for i in range(len(qw)):
        questions.append({"author": f"Автор {qw[i].author}", "tags": Tags1.get_all_tags_id(i),
                          "quest_data": qw[i].quest_data,
                          "nums_of_answers": qw[i].nums_of_answers})
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
    qw=Quests.get_answers_by_quest_id(num)
    for i in range(len(qw)):
        answers.append({"author": f"Автор {qw[i].username}",
                    "ans_data": qw[i].data})
    page_number = request.GET.get('page')
    page = paginate(answers, request, per_page=10)
    return render(request,'main/question.html', context={'num': num,'answers':page.object_list,'ask':Quests.get_all_quests_id(num).quest_data,
                                                         'paginator':page.paginator,'page':page})
def ask(request):
    return render(request,'main/ask.html')
def login(request):
    return render(request,'main/login.html')
def signup(request):
    return render(request,'main/signup.html')
def page(request,num):
    return render(request,'main/tagquest.html', context={'num': num})
def like_question(request, question_id):
  question = get_object_or_404(Quests, pk=question_id)
  if request.user.is_authenticated:
      QuestionLike.objects.create(user=request.user, question=question)
      # ... (логика обработки успешного лайка) ...
  return redirect(question.get_absolute_url())
def hot(request):
    questions = []
    #qw=Newquests.get_all_quests()
    qw=QuestsManager.get_hot()
    for i in range(len(qw)):
        questions.append({"author": f"Автор {qw[i].author}", "tags": Tags1.get_all_tags_id(i),
                          "quest_data": qw[i].quest_data,
                          "nums_of_answers": qw[i].nums_of_answers})
    page = paginate(questions, request, per_page=10)
    context1 = {'questions': page.object_list,
                'paginator': page.paginator,
                'page': page, }
    return render(request, 'main/hot.html', context=context1)

def asa(request):
    print(QuestsManager.get_hot())
    questions = []
    qw=Quests.get_all_quests()
    for i in range(len(qw)):
        questions.append({"author": f"Автор {qw[i].author}", "tags": Tags1.get_all_tags_id(i),
                    "quest_data": qw[i].quest_data,
                    "nums_of_answers": qw[i].nums_of_answers})

    # Используем функцию paginate для пагинации
    page = paginate(questions, request, per_page=10)

    context1 = {'questions': page.object_list,
                'paginator': page.paginator,  # Доступ к paginator через page.paginator
                'page': page, }

    return render(request, 'main/questions_list.html', context=context1)
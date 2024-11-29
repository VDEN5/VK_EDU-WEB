from idlelib.iomenu import errors
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.db import connection
from .models import Quests, QuestionLike, Tags1, QuestsManager, Answer
from .utils import paginate
from .forms import UserForm, LoginForm, QuestForm, AnsForm
from django.urls import reverse
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
                'tag': tag,
                'username':request.session.get('username'),}

    return render(request, 'main/tagquest.html', context=context1)
def question(request,num):
    username=request.session.get('username')
    err=None
    if request.method == 'POST':
        form = AnsForm(request.POST)
        if form.is_valid():
            #question = form.save()
            Answer.add_ans_id(username,form['data'].data,num)
            return redirect('/question/'+str(num)+'?page=2024#new_answer')#вместо 2024 можно поставить число страниц, но дольше работать будет
        err=form.errors
    else:
        form =AnsForm()
    answers = []
    qw=Quests.get_answers_by_quest_id(num)
    for i in range(len(qw)):
        answers.append({"author": f"Автор {qw[i].username}",
                    "ans_data": qw[i].data})
    page_number = request.GET.get('page')
    page = paginate(answers, request, per_page=10)
    return render(request,'main/question.html', context={'num': num,'answers':page.object_list,'ask':Quests.get_all_quests_id(num).quest_data,
                                                         'paginator':page.paginator,'page':page,'username':request.session.get('username'),
                                                         'form': form,
                                                         'errors':err,})
def ask(request):
    return render(request,'main/ask.html',context={'username':request.session.get('username'),})
def login1(request):
    print(request.path)
    next_url = request.GET.get('continue')  # Получаем параметр continue
    if next_url is None:
        next_url='/'
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                request.session['username'] = user.username
                return redirect(next_url)
                #return redirect(reverse('profile.edit'))
            form.add_error('password', 'Invalid username or password.')
    return render(request, 'main/login.html', {'form': form})

@login_required
def signup(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        form.add_error('password', 'Bad password.')

    return render(request, 'main/signup.html', {"form": form})
    #return render(request,'main/signup.html')
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
                'page': page,
                'username':request.session.get('username'),}
    return render(request, 'main/hot.html', context=context1)

def asa(request):
    username=request.session.get('username')
    print(username)
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            question = form.save()
            print(question.pk)
            return redirect('/question'+str(question.pk))
        form.add_error('data', 'bad answer data')
    else:
        form = QuestForm()
    #print(QuestsManager.get_hot())
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
                'page': page,
                'username':username,
                'form':form,}

    return render(request, 'main/questions_list.html', context=context1)
def logout1(request):
    logout(request)
    return redirect('/')
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                request.session['username'] = user.username
            form.add_error('password', 'Bad password.')
            form.add_error('email', 'Bad e-mail')
                #return redirect(reverse('asa'))
            #return redirect(reverse('asa')) # Или перенаправить на другую страницу
    else:
        form = UserForm(instance=request.user)
    return render(request, 'main/edit_profile.html', {'form': form})
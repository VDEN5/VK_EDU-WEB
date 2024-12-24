from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('like/question/', views.like_question, name='like.question'),
    path('like/answer/', views.like_answer, name='like.answer'),
    path('answer/update/', views.update_answer, name='answer.update'),
    path('', views.asa,name='asa'),
    path('about', views.about,name='about'),
    path('question/<int:num>',views.question, name='question'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('ask',views.ask, name='ask'),
    path('login',views.login1, name='login'),
    path('signup',views.signup, name='signup'),
    path('tag/<slug:num>', views.tag, name='tag'),
    path('hot', views.hot, name='hot'),
    path('as',views.asa, name='as'),
path('admin/', admin.site.urls),
path('logout', views.logout1, name='logout'),
    path('edit',views.edit_profile,name='edit')
    #path('admin',name='admin')
]
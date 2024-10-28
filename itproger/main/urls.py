from django.urls import path
from . import views
app_name='itproger'
urlpatterns = [
    path('', views.asa,name='asa'),
    path('about', views.about,name='about'),
    path('question/<int:num>',views.question, name='question'),
    path('ask',views.ask, name='ask'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('tag/<slug:num>', views.tag, name='tag'),
    path('hot', views.hot, name='hot'),
    path('as',views.asa, name='as'),
]
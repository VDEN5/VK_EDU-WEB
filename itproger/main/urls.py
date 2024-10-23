from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('question',views.question),
    path('ask',views.ask),
    path('login',views.login),
    path('signup',views.signup),
]
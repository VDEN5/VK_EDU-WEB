from django.urls import path
from . import views
urlpatterns = [
    path('', views.asa),
    path('about', views.about),
    path('question/<int:num>',views.question),
    path('ask',views.ask),
    path('login',views.login),
    path('signup',views.signup),
    path('tag/<slug:num>', views.tag),
    path('hot', views.hot),
    path('as',views.asa),
]
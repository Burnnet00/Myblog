from django.urls import path
from  . import views #import blog catalog
'''поключаэт додуль "пес" совмещая просмотры с главной станичкой (адресом) сайта'''
urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view())]
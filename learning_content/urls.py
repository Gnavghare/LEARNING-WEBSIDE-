from django.urls import path
from . import views

app_name = 'learning_content'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
    path('courses/<slug:course_slug>/lessons/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
    path('courses/<slug:course_slug>/lessons/<slug:lesson_slug>/quiz/', views.take_quiz, name='take_quiz'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
] 
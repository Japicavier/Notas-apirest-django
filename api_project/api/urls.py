from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('curso/', views.curso, name='curso'),
    path('curso/new/', views.post_curso, name='post_curso'),
    path('cursodrf/',views.CursoList.as_view(), name='curso_list'),
]

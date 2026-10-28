from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tarea',views.TareaView.as_view(), name='tarea'),
    path('tarea/<int:pk>',views.TareaDetailView.as_view(), name='tarea_detail'),
]

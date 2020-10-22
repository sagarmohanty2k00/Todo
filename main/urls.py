from . import views
from django.urls import path

urlpatterns = [
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('todo/', views.todoView),
    path('todo/add_todo/', views.add_todo),
    path('todo/delete_todo/<int:todo_id>/', views.delete_todo),
]
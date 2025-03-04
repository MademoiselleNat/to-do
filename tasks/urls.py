from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('tasks/', views.TaskList.as_view(), name = "Task_List"),
    path('task-create/', views.TaskCreate.as_view(), name = "task-create"),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name = 'task-delete'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('edit_task/<str:pk>/',views.editTask,
    name='edit-task')
]
from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, UserLoginView, UserRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
]
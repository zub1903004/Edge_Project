from django.urls import path
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('<int:pk>/edit/', task_update, name='task_update'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
]
from django.contrib.auth import views as auth_views
urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('last_check/', views.login_check, name='login_check'),
]
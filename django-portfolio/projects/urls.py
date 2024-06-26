from django.urls import include, path
from projects import views


app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path("<int:pk>", views.project_detail, name='project_detail'),
    path("explore", views.django_play, name='django_play'),
]
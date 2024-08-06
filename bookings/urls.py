from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
  ]
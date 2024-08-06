from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),  # Homepage
    path('home/', views.IndexView.as_view(), name='home'),  # Homepage
    path('courses/', views.CoursesView.as_view(), name='courses'),  # Courses page
  ]
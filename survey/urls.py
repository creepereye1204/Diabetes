from django.urls import path
from . import views

urlpatterns = [
    path('', views.SurveyListView.as_view(), name='survey'),
    path('result/', views.survey_result_view, name='result')
    ]


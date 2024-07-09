from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Survey, Data
import numpy as np
import joblib

svm_model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')


class SurveyListView(ListView):
    model = Survey
    template_name = 'survey/survey.html'
    ordering = '-pk'

    def post(self, request, *args, **kwargs):

        x = np.array([[value for i, (key, value) in enumerate(request.POST.items()) if i > 0]])

        Data.objects.create(
            age=request.POST['나이'],
            diabetes_pedigree_function=request.POST['당뇨 내력 가중치 값'],
            bmi=request.POST['체질량지수(체중(kg)/(키(m))^2)'],
            insulin=request.POST['혈청 인슐린(mu U/ml)'],
            skin_thickness=request.POST['팔 삼두근 뒤쪽의 피하지방 측정값(mm)'],
            pregnancies=request.POST['임신 횟수'],
            glucose=request.POST['포도당 부하 검사 수치'],
            blood_pressure=request.POST['혈압(mm Hg)'],
        )
        normalized_x = scaler.transform(x)
        y = svm_model(normalized_x)
        request.session['result'] = y
        return redirect('result')


def survey_result_view(request):
    print(request.session['result'])
    return render(request, 'survey/survey.html')

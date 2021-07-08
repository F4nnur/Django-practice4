from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import *


# Create your views here.

def inndex(request):
    return render(request, 'site_with_tests/index.html', {'title': "Добро пожаловать!"})


def configure_test(request):
    questions = Question.objects.filter(test=None)
    return render(request, 'site_with_tests/configure_test.html', {'questions': questions, 'title': "Формирование вопроса"})


def editing_test(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка')
    else:
        form = QuestionForm()
    return render(request, 'site_with_tests/editing.html', {'form': form, 'title': "Добавление вопроса"})


def all_tests(request):
    return render(request, 'site_with_tests/all_tests.html', {'title': "Все тесты"})


def passing_test(request):
    return render(request, 'site_with_tests/passing_test.html', {'title': "Прохождение теста"})


def results_test(request):
    return render(request, 'site_with_tests/results_test.html', {'title': "Результаты"})


def statistics(request):
    return render(request, 'site_with_tests/statistics.html', {'title': "Статистика"})

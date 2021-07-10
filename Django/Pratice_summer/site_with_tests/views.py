from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def inndex(request):
    return render(request, 'site_with_tests/index.html', {'title': "О сайте"})


def configure_test(request):
    questions = Question.objects.filter(test=None)
    return render(request, 'site_with_tests/configure_test.html',
                  {'questions': questions, 'title': "Формирование вопроса"})


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
    tests = Test.objects.all()
    return render(request, 'site_with_tests/all_tests.html', {'title': "Список тестов", 'tests': tests})


def passing_test(request):
    return render(request, 'site_with_tests/passing_test.html', {'title': "Прохождение теста"})


def results_test(request):
    return render(request, 'site_with_tests/results_test.html', {'title': "Результаты"})


def statistics(request):
    tests = Test.objects.all()
    questions = Question.objects.all()
    name = request.user.username
    answers = Entering.objects.filter(user=request.user)
    context = {
        'title': "Статистика",
        'answers': answers,
        'questions': questions,
        'name': name,
        'tests': tests,
    }
    return render(request, 'site_with_tests/statistics.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'site_with_tests/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'site_with_tests/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


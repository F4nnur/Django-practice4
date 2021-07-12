from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def inndex(request):
    return render(request, 'site_with_tests/index.html', {'title': "О сайте"})


def configure_test(request):
    questions = Question.objects.filter(test=None)
    return render(request, 'site_with_tests/configure_test.html',
                  {'questions': questions, 'title': "Формирование теста"})


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


def passing_test(request, test_id):


    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test_id)

    context = {
        'user': test.user,
        'title': "Прохождение ",
        'test': test.name_of_test,
        'questions': questions,
        'test_id': test.id

    }
    if request.method == 'POST':
        form = PasForm(request.POST, initial={'user': test.user, 'test': test.name_of_test})
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка')
    else:
        form = PasForm()
    return render(request, 'site_with_tests/passing_test.html', {'form': form, 'content': context})


def results_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test_id)

    context = {
        'title': "Результаты теста ",
        'test': test.name_of_test,
        'questions': questions,
        'test_id': test_id

    }
    return render(request, 'site_with_tests/results_test.html', context)


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


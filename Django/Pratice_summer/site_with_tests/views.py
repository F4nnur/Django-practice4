from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inndex(request):
    return render(request, 'site_with_tests/index.html')


def configure_test(request):
    return render(request, 'site_with_tests/configure_test.html')


def editing_test(request):
    return render(request, 'site_with_tests/editing.html')


def all_tests(request):
    return render(request, 'site_with_tests/all_tests.html')


def passing_test(request):
    return render(request, 'site_with_tests/passing_test.html')


def results_test(request):
    return render(request, 'site_with_tests/results_test.html')


def statistics(request):
    return render(request, 'site_with_tests/statistics.html')


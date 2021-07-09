from django.urls import path
from .views import *

urlpatterns = [
    path('', inndex, name='home'),
    path('configure/', configure_test, name='configure'),
    path('editing/', editing_test, name='editing'),
    path("all_tests/", all_tests, name='all_tests'),
    path('passing/', passing_test, name='passing_test'),
    path('results/', results_test, name='results'),
    path("statistics/", statistics, name='statistics'),
    path("register/", RegisterUser.as_view(), name='register'),
    path("login/", LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('', inndex, name='home'),
    path('configure/', configure_test, name='configure'),
    path('editing/', editing_test, name='editing'),
    path("all_tests/", all_tests, name='all_tests'),
    path('passing/<int:test_id>/', passing_test, name='passing_test'),
    path('results/<int:test_id>/', results_test, name='results'),
    path("statistics/", statistics, name='statistics'),
    path("register/", RegisterUser.as_view(), name='register'),
    path("login/", LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

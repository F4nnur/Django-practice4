from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Question, Test, Entering
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quest', 'var1', 'var2', 'var3', "var4", 'var1_isTrue', 'var2_isTrue', 'var3_isTrue',
                  'var4_isTrue']
        widgets = {
            'quest': forms.TextInput(attrs={'class': "form-control", 'type': 'text'}),
            'var1': forms.TextInput(attrs={'class': "form-control", 'type': 'text'}),
            'var2': forms.TextInput(attrs={'class': "form-control", 'type': 'text'}),
            'var3': forms.TextInput(attrs={'class': "form-control", 'type': 'text'}),
            'var4': forms.TextInput(attrs={'class': "form-control", 'type': 'text'}),
            'var1_isTrue': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            'var2_isTrue': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            'var3_isTrue': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            'var4_isTrue': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
        }

class PasForm(forms.ModelForm):
    class Meta:
            model = Entering
            fields = ['test', 'user', 'answer_of_user1', 'answer_of_user2', 'answer_of_user3', "answer_of_user4"]
            widgets = {
            'answer_of_user1': forms.TextInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            'answer_of_user2': forms.TextInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            'answer_of_user3': forms.TextInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            'answer_of_user4': forms.TextInput(attrs={'class': "form-check-input", 'type': 'checkbox'}),
            }



class ConfigureForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name_of_test', 'description']
        widgets = {
            "name_of_test": forms.TextInput(attrs={'class': "form-control", 'type': 'text'}),
            'description': forms.TextInput(attrs={'class': "form-control", 'type': 'text'})
        }


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

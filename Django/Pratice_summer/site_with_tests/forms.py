from .models import Question
from django import forms
from django.forms import ModelForm


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['quest', 'var1', 'var2', 'var3', "var4", 'var1_isTrue','var2_isTrue', 'var3_isTrue', 'var4_isTrue']
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
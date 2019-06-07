from .models import Task, UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password','description')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'text', 'cost', 'name')

class Change_info(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields =('text','name','surname','username','email')

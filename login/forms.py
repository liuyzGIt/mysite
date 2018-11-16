from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(max_length=128, label='用户名',widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(max_length=256, label='密码', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    # captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(max_length=128, label='用户名', widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(max_length=256, label='密码', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(max_length=256, label='密码', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='邮箱', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

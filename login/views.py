from django.shortcuts import render, redirect
from .models import User
from . import forms
import hashlib


# Create your views here.


def login(request):
    # message = ''
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     if username and password:
    #         username = username.strip()
    #         try:
    #             user = User.objects.get(name=username)
    #             if user.password != password:
    #                 message = '密码错误'
    #             else:
    #                 return redirect('/index/')
    #         except:
    #             message = '用户不存在'
    #     else:
    #         message = '请将信息填写完整'
    # return render(request, 'login/login.html', {'message': message})
    if request.session.get('is_login'):
        return redirect('/index/')

    if request.method == 'POST':
        message = '请将登录信息填写完整'
        login_form = forms.UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = hash_code(login_form.cleaned_data['password'])

            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码错误'
            except:
                message = '用户未注册'
        return render(request, 'login/login.html', locals())
    login_form = forms.UserForm
    return render(request, 'login/login.html', locals())


def logout(request):
    request.session.flush()
    return redirect('/login/')


def index(request):
    return render(request, 'login/index.html')


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            password = register_form.cleaned_data['password1']
            if password == register_form.cleaned_data['password2']:

                user = User()
                user.name = register_form.cleaned_data['username']
                user.password = hash_code(password)
                user.email = register_form.cleaned_data['email']
                user.sex = register_form.cleaned_data['sex']
                if User.objects.filter(name=user.name):
                    message = '该名称已注册'
                elif User.objects.filter(email=user.email):
                    message = '该邮箱已注册'
                else:
                    try:
                        user.save()
                        return redirect('/login/')
                    except:
                        message = '保存失败'
            else:
                message = "两次输入的密码不一致"
        else:
            message = '请将信息填写完整'
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

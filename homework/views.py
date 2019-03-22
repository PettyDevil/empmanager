from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from homework import models
from homework.forms import RegisterForm
from homework.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': '用户不存在！'})
        if user.password == password:
            info = User.objects.filter()
            return render(request, 'userList.html', {'info': info})
        else:
            return render(request, 'login.html', {'error': '密码错误！'})
    return render(request, 'login.html')


def regist(request):
    if request.method == 'POST':
        username = request.POST['username']
        realname = request.POST['realname']
        password = request.POST['password']
        sex = request.POST['sex']
        age = request.POST['age']
        telephone = request.POST['telephone']
        require = request.POST['require']
        register_form = RegisterForm(request.POST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            if register_form.is_valid(): # 如果form有效
                User.objects.create(
                    username=username,
                    realname=realname,
                    password=password,
                    sex=sex,
                    age=age,
                    telephone=telephone,
                    require=require

                )
                return render(request, "login.html",{ 'right':'注册成功！请登录。' })
            else:
                data = {
                    'error': '验证码错误，请重新输入！',
                    'register_form': register_form
                }
                return render(request, 'regist.html', data)
        else:
            data = {
                'error': '验证码错误，请重新输入！',
                'register_form': register_form
            }
            return render(request, 'regist.html', data)
    else:
        register_form = RegisterForm(request.POST)
        return render(request, 'regist.html', {'register_form': register_form})


def userDetail(request):
    id = request.GET.get("id")
    infor = User.objects.filter(id=id)
    img = models.User.objects.get(id=id)
    img = str(img.name)
    print('*********'+img)
    if img == 'None':
        img == ''
    return render(request, 'userDetail.html', {'infor': infor})


def userList(request):
    info = User.objects.filter()
    return render(request, 'userList.html', {'info': info})


def userdelete(request):
    id = request.GET.get("id")
    User.objects.filter(id=id).delete()
    return redirect('/login/')


def userphoto(request):
    if request.method == 'POST':
        id = request.GET.get("id")
        img = request.FILES.get('img')
        name = request.FILES.get('img').name
        models.User.objects.filter(id=id).update(img=img,name=name)
        User.objects.create(img=img,name=name)
        inf = User.objects.filter(id=id)
        return render(request,'userDetail.html',{'infor':inf})
    else:
        return redirect('/userDetail/')

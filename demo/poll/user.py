from django.shortcuts import render
from django.http import HttpResponse
from .data_infos import info
from .models import Info
from .model import PollInfo, User
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


# 显示主页
def index(request):
    # res = info().citys()
    res = PollInfo.objects.all()
    # print(res)
    temp = []
    for obj in res:
        temp.append(obj)
    context = {'info': temp}
    return render(request, 'demos/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = User.objects.filter(username=username).first()
                if not user:
                    return HttpResponse("<script>alert('用户名不正确');location.href='/login/' </script>")
                # 暂时不校验密码
                if user.password != password:
                    return HttpResponse("<script>alert('密码错误！');location.href='/login/' </script>")
                request.session['user_id'] = user.id
                return HttpResponse("<script>alert('登录成功！'); location.href='/' </script>")
            except Exception as e:
                print(e)
                return HttpResponse("<script>alert('登陆失败,稍后重试'); location.href='/login/'</script>")
        return HttpResponse("<script>alert('登陆失败,请输入用户名密码''); location.href='/login/' </script>")
    return render(request, 'demos/login.html')


def logout(request):
    request.session.flush()
    return render(request, 'demos/login.html')


def register(request):
    return render(request, 'demos/register.html')

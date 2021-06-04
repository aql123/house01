from django.shortcuts import render, redirect
from .model import Users, PollInfo
from django.http import HttpResponse
from django.db.models import Q


#首页数据展示
def index(request):
    kw = request.POST.get('kw')
    if kw:
        # 搜索
        list = PollInfo.objects.filter( Q(name__icontains=kw) | Q(city__icontains=kw)).order_by('-id').all()
    else:
        # 没有搜索
        list = PollInfo.objects.order_by('-id').all()[0:30]

    return render(request, 'home/house.html', {'houseList':list})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            print(request.POST.get('username'))
            users = Users.objects.filter(username=username).first()
            if not users:
                return HttpResponse('<script>alert("用户名不正确"); </script>')
            # 暂时不校验密码
            if users.password != password:
                return HttpResponse("<script>alert('密码错误！'); </script>")
            request.session['users_id'] = users.id
            request.session['username'] = users.username
            return HttpResponse("<script>alert('登录成功！'); location.href='/home/index/' </script>")
        except Exception as e:
            print(e)
            return HttpResponse('<script>alert("登陆失败,稍后重试"); </script>')
    return render(request, 'home/login.html')


def register(request):
    if request.method == 'POST':
        if request.session.get('users_id',0):
            return HttpResponse("<script>alert('已登录！'); location.href='/home/index' </script>")
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        print(username)
        password = request.POST.get('password')
        password2 = request.POST.get('password1')
        city = request.POST.get('city')
        area = request.POST.get('area')
        price = request.POST.get('price')

        if username and mobile and password and password2 and city and price and area:  # 提交注册表单
            if password != password2:
                return HttpResponse("<script>alert('两次密码输入不一致！'); location.href='/home/register/' </script>")
            user = Users.objects.filter(username=username).first()
            if user:
                return HttpResponse("<script>alert('用户名已存在！'); location.href='/home/register/' </script>")
            # 为User类属性赋值
            users = Users(
                username=username,
                mobile=mobile,
                password=password,
                city=city,
                area=area,
                price=price
            )
            users.save()
            return HttpResponse("<script>alert('注册成功，请登录！'); location.href='/home/login/' </script>")
        return HttpResponse("<script>alert('请填写全部信息！'); location.href='/home/register/' </script>")

    return render(request, 'home/register.html')


def logout(request):
    request.session.flush()
    return render(request, 'home/login.html')


# 推荐列表
def tuijian(request):
    if not request.session.get('users_id'):
        return HttpResponse("<script>alert('请登录！'); location.href='/home/login/' </script>")
    datalist = []
    houseList = viewLog(request)

    return render(request, 'home/tuijian.html',{ 'houseList':houseList})


def viewLog(request):
    """
    基于用户信息的推荐
    :return:
    """
    if not request.session.get('users_id'):
        return HttpResponse("<script>alert('请登录！'); location.href='/home/login' </script>")
    # 获取当前登陆人信息
    userInfo = Users.objects.filter(id=request.session.get('users_id',0)).first()
    price = userInfo.price  #价格
    area = userInfo.area    #户型大小
    city = userInfo.city    #城市
    if not city: #如果没有城市就默认北京
        city = '北京'
    newList = []
    if city:
        # 根据用户所选户型大小上下20浮动 + 价格上下1000 + 所选城市 筛选
        houseList = PollInfo.objects.filter(area__range=(area-20,area+20)).filter(price__range=(price-1000,price+1000)).filter(city=city).all()

    if not houseList:
        # 如果以上搜索没有数据，就选择城市下价格排序的前15个
        houseList = PollInfo.query.filter(city=city).order_by('-price').all()[:15]

    return houseList
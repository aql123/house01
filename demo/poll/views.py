from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import Info
from .model import PollInfo


def login_check(func):
    def wrapper(request, *args, **kwargs):
        is_login = request.session.get('user_id',0)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return wrapper

# 显示主页
@login_check
def index(request):
    # res = info().citys()
    res = PollInfo.objects.all()
    # print(res)
    temp = []
    for obj in res:
        temp.append(obj)
    context = {'info': temp}
    return render(request, 'demos/index.html', context)


# 显示地区房源
@login_check
def cityinfo(request, name):
    page = request.GET.get('page', 1)  # 获取page参数值
    limit_page = 12
    if name == 'bj':
        city = '北京'
    elif name == 'sh':
        city = '上海'
    elif name == 'gz':
        city = '广州'
    elif name == 'sz':
        city = '深圳'
    kw = request.POST.get('kw')
    if kw:
        limit_page = 100
        page_data = PollInfo.objects.filter( name__icontains=kw ).filter(city=city).all()
    else:
        page_data = PollInfo.objects.filter(city=city).all()
    paginator = Paginator(page_data, limit_page)
    try:
        # 通过获取上面的page参数，查询此page是否为整数并且是否可用
        subject_obj = paginator.page(page)
    except PageNotAnInteger:
        subject_obj = paginator.page(1)
    except (EmptyPage, InvalidPage):
        subject_obj = paginator.page(paginator.num_pages)
        # ob = PollInfo.objects.filter(city='北京')
    context = {'citys': subject_obj, 'name': name}
    return render(request, 'demos/bjform.html', context)


# 显示房源详情
@login_check
def houseinfo(request, hid):
    ob = Info.objects.get(id=hid)
    context = {'hdt': ob}
    return render(request, 'demos/housedt.html', context)


@login_check
def houseinfo_edit(request, hid):
    ob = PollInfo.objects.get(id=hid)
    context = {'obj':ob}
    return render(request, 'demos/edit.html', context)


@login_check
def houseinfo_new(request):
    return render(request, 'demos/add.html')

# 新增
@login_check
def houseinfo_new_save(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price')
        types = request.POST.get('types')
        area = request.POST.get('area')
        floor = request.POST.get('floor')
        elevator = request.POST.get('elevator')
        fuel = request.POST.get('fuel')
        log = request.POST.get('log')
        lat = request.POST.get('lat')
        city = request.POST.get('city')

        try:
            with transaction.atomic():

                house = PollInfo(
                    name= name,
                    price= price,
                    types= types,
                    area= area,
                    floor= floor,
                    elevator= elevator,
                    fuel= fuel,
                    log= log,
                    lat= lat,
                    city= city,

                )
                house.save()
                label = 'bj'
                if name == '北京':
                    label = 'bj'
                elif name == '上海':
                    label = 'sh'
                elif name == '广州':
                    label = 'gz'
                elif name == '深圳':
                    label = 'sz'
                print('成功了')
                return redirect('/cityinfo/'+label)
        except Exception as e:
            print(e)
            return HttpResponse('<script>alert("操作失败"); </script>')
    return HttpResponse('<script>alert("操作失败,请勿直接访问"); </script>')


# 新增
@login_check
def houseinfo_edit_save(request):
    if request.method == 'POST':

        id = request.POST.get('id',0)
        name = request.POST.get('name')
        price = request.POST.get('price')
        types = request.POST.get('types')
        area = request.POST.get('area')
        floor = request.POST.get('floor')
        elevator = request.POST.get('elevator')
        fuel = request.POST.get('fuel')
        log = request.POST.get('log')
        lat = request.POST.get('lat')
        city = request.POST.get('city')
        print(price)
        try:
            with transaction.atomic():
                house = PollInfo.objects.get(id=id)

                house.name= name
                house.price= int(price)
                house.types= types
                house.area= float(area)
                house.floor= floor
                house.elevator= elevator
                house.fuel= fuel
                house.log= log
                house.lat= lat
                house.city= city
                house.save()
                label = 'bj'
                if name == '北京':
                    label = 'bj'
                elif name == '上海':
                    label = 'sh'
                elif name == '广州':
                    label = 'gz'
                elif name == '深圳':
                    label = 'sz'
                print('成功了')
                return redirect('/cityinfo/'+label)
        except Exception as e:
            print(e)
            return HttpResponse('<script>alert("操作失败"); </script>')
    return HttpResponse('<script>alert("操作失败，请勿直接访问"); </script>')


@login_check
def houseinfo_del(request, hid):
    ob = PollInfo.objects.get(id=hid)
    if ob:
        label = 'bj'
        if ob.city == '北京':
            label = 'bj'
        elif ob.city == '上海':
            label = 'sh'
        elif ob.city == '广州':
            label = 'gz'
        elif ob.city == '深圳':
            label = 'sz'
        ob.delete()
        return redirect('/cityinfo/' + label)
    return HttpResponse('<script>alert("操作失败"); </script>')


@login_check
def bj(request):
    return render(request, 'demos/北京_render.html')


@login_check
def sh(request):
    return render(request, 'demos/上海_render.html')


@login_check
def gz(request):
    return render(request, 'demos/广州_render.html')


@login_check
def sz(request):
    return render(request, 'demos/深圳_render.html')

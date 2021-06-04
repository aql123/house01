from django.conf.urls import url
from . import views, user, home

urlpatterns = [
    # 显示主页
    url(r'^$', views.index, name='index'),


    url('^home/tuijian/$', home.tuijian ),
    url('^home/index/$', home.index ),
    url('^home/login/$', home.login ),
    url('^home/logout/$', home.logout ),
    url('^home/register/$', home.register ),

    # 显示城市房源表格
    url('^cityinfo/(?P<name>.*)/$', views.cityinfo, name='cityinfo'),
    # 显示房源详情信息
    url('^houseinfo_new/$', views.houseinfo_new, name='houseinfo_new'),
    url('^houseinfo/(?P<hid>[0-9]+)/$', views.houseinfo, name='houseinfo'),
    url('^houseinfo_edit/(?P<hid>[0-9]+)/$', views.houseinfo_edit, name='houseinfo_edit'),
    url('^houseinfo_new_save/$', views.houseinfo_new_save, name='houseinfo_new_save'),
    url('^houseinfo_edit_save/$', views.houseinfo_edit_save, name='houseinfo_edit_save'),
    url('^houseinfo_del/(?P<hid>[0-9]+)/$', views.houseinfo_del, name='houseinfo_del'),
    # 显示房源详情信息
    url('^houseinfo/bj/$', views.bj, name='bj'),
    # 显示房源详情信息
    url('^houseinfo/sh/$', views.sh, name='sh'),
    # 显示房源详情信息
    url('^houseinfo/gz/$', views.gz, name='gz'),
    # 显示房源详情信息
    url('^houseinfo/sz/$', views.sz, name='sz'),

    url('^login/$', user.login, name='login'),
    url('^logout/$', user.logout, name='logout'),
    url('^register/$', user.register, name='register'),
]

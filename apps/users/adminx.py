# -*- coding: utf-8 -*-
__author__ = 'lins'
__date__ = ' 2:37 AM'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # 列表字段展示
    search_fields = ['code', 'email', 'send_type']  #  搜索框显示
    list_filter = ['code', 'email', 'send_type', 'send_time'] # 筛选器



class BaseSetting(object):
    enable_themes = True  # 开启主题功能
    use_bootswatch = True




class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"



class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


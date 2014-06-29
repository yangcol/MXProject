__author__ = 'yangq'
#encoding:utf-8
from django.contrib.auth.models import User, Group, Permission
from django.contrib import admin
from models import Province, City, Xian, Reservoir
from models import ProvinceUser, CityUser, XianUser, ReservoirUser

import logging
logger = logging.getLogger(__name__)


#用户权限
class PermissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Permission, PermissionAdmin)

'''
#用户组的Admin是自动注册的#
class GroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group, GroupAdmin)

'''
#用户权限Admin
class ProvinceUserAdmin(admin.ModelAdmin):
    pass


class CityUserAdmin(admin.ModelAdmin):
    pass


class XianUserAdmin(admin.ModelAdmin):
    pass


class ReservoirUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProvinceUser, ProvinceUserAdmin)
admin.site.register(CityUser, CityUserAdmin)
admin.site.register(XianUser, XianUserAdmin)
admin.site.register(ReservoirUser, ReservoirUserAdmin)


#行政区划Admin
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )


class XianAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ReservoirAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Xian, XianAdmin)
admin.site.register(Reservoir, ReservoirAdmin)


def create_province_user(name, password, email=None):
    pass


def create_city_user(name, password, email=None):
    pass


def create_xian_user(name, password, email=None):
    pass


def create_user(name, password, email=None, level=0):
    if level == 0:
        #县级用户
        pass
    elif level == 1:
        #市级用户
        pass
    elif level == 2:
        #省级用户
        pass
    else:
        #异常
        pass


def init():
    """ Initial environment
    """
    p_xian = Permission.objects.create(name='view_xian')
    p_city = Permission.objects.create(name='view_city')
    p_pro = Permission.objects.create(name='view_province')

    g_xian = Group.objects.create(name="xian")
    g_city = Group.objects.create(name="city")
    g_province = Group.objects.create(name="province")

    # Add permission

    # Create 3 xian users
    users = [
        User.objects.create_user('xian1', None, '1'),
        User.objects.create_user('xian2', None, '1'),
        User.objects.create_user('xian3', None, '1')]
    [user.save() for user in users]
    # Create 3 city users
    users = [
        User.objects.create_user('city1', None, '1'),
        User.objects.create_user('city2', None, '1'),
        User.objects.create_user('city3', None, '1')]
    [user.save() for user in users]

    # Create 3 province users
    users = [
        User.objects.create_user('province1', None, '1'),
        User.objects.create_user('province2', None, '1'),
        User.objects.create_user('province3', None, '1')]
    [user.save() for user in users]



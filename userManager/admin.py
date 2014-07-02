#encoding:utf-8
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from django.contrib import admin
from models import Province, City, Xian, Reservoir, UserProfile
from models import UserProfile
import logging

# Get an instance of a logger
logger = logging.getLogger('myproject.custom')
#用户权限
class PermissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Permission, PermissionAdmin)

'''
#用户组的Admin是自动注册的#
class GroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group, GroupAdmin)


#用户权限Admin
class ProvinceUserAdmin(admin.ModelAdmin):
    pass


class CityUserAdmin(admin.ModelAdmin):
    pass


class XianUserAdmin(admin.ModelAdmin):
    pass


class ReservoirUserAdmin(admin.ModelAdmin):
    pass
'''


class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)
##admin.site.register(CityUser, CityUserAdmin)
#admin.site.register(XianUser, XianUserAdmin)
#admin.site.register(ReservoirUser, ReservoirUserAdmin)


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


def create_permission(name, content_type):
    p = Permission.objects.filter(name=name)[:1]
    if not p:
        pass
    else:
        #print "P:", p[0]
        return p[0]

    try:
        p = Permission.objects.create(name=name, content_type=content_type)
    except Exception, e:
        logger.debug("create permission [%s] failed, %s" % (name, e.message))

    return p


def create_province_user(name, password, email=None):
    create_user(name, email, password, level='province')


def create_city_user(name, password, email=None):
    create_user(name, email, password, level='city')


def create_xian_user(name, password, email=None):
    create_user(name, email, password, level='xian')


def create_reser_user(name, password, email=None):
    create_user(name, email. password, level='reservoir')


def create_user(name, email, password, level, sex, age, department):
    user = User.objects.filter(username=name)[:1]
    if not user:
        pass
    else:
        return user[0]

    # Create group
    if level == 'reservoir':
        g = Group.objects.filter(name='reservoir')[0]
        user = User.objects.create_user(name, email, password)
        user.groups.add(g)
        user.save()
    elif level == 'xian':
        g = Group.objects.filter(name='xian')[0]
        user = User.objects.create_user(name, email, password)
        user.groups.add(g)
        user.save()
    elif level == 'city':
        g = Group.objects.filter(name='city')[0]
        user = User.objects.create_user(name, email, password)
        user.groups.add(g)
        user.save()
    elif level == 'province':
        g = Group.objects.filter(name='province')[0]
        user = User.objects.create_user(name, email, password)
        user.groups.add(g)
        user.save()
    else:
        logger.error("error input")

    profile = UserProfile.objects.create(user=user, sex=sex, age=age, department=department)
    profile.save()
    return user


def create_group(name, permissions):
    g = Group.objects.filter(name=name)
    if not g:
        pass
    else:
        return g[0]

    try:
        g = Group.objects.create(name=name)
        g.permissions = permissions
    except Exception, e:
        logger.debug("create group [%s] failed, %s" % (name, e.message))

    return g


def init():
    # Create super user
    logger.info("Start init")
    try:
        admin = User.objects.create_superuser('enyo', None, '.')
        admin.save()
    except Exception, e:
        pass
        #print e.message
    re_table = ContentType.objects.get(name=Reservoir.__name__.lower())
    xian_table = ContentType.objects.get(name=Xian.__name__.lower())
    city_table = ContentType.objects.get(name=City.__name__.lower())
    pro_table = ContentType.objects.get(name=Province.__name__.lower())
    p_re = create_permission(name='view_reservoir', content_type=re_table)
    p_xian = create_permission(name='view_xian', content_type=xian_table)
    p_city = create_permission(name='view_city', content_type=city_table)
    p_pro = create_permission(name='view_province', content_type=pro_table)

    g_reservoir = create_group(name='reservoir', permissions=[p_re])
    g_xian = create_group(name="xian", permissions=[p_xian])
    g_city = create_group(name="city", permissions=[p_city])
    g_province = create_group(name="province", permissions=[p_pro])

    # Add permission
    users = [
        create_user('reser1', None, '1', 'reservoir', sex='男', age=30, department='水库办公室201'),
        create_user('reser2', None, '1', 'reservoir', sex='女', age=41, department='水库办公室204'),
        create_user('reser3', None, '1', 'reservoir', sex='男', age=50, department='水库办公室305')
    ]

    # Create 3 xian users
    users = [
        create_user('xian1', None, '1', 'xian', sex='男', age=30, department='县级办公室201'),
        create_user('xian2', None, '1', 'xian', sex='女', age=41, department='县级办公室204'),
        create_user('xian3', None, '1', 'xian', sex='男', age=50, department='县级办公室305')]

    # User.objects.get(username='xian1')
    # Create 3 city users
    users = [
        create_user('city1', None, '1', 'city', sex='男', age=30, department='市级办公室201'),
        create_user('city2', None, '1', 'city', sex='女', age=41, department='市级办公室204'),
        create_user('city3', None, '1', 'city', sex='男', age=50, department='市级办公室305')]

    # Create 3 province users
    users = [
        create_user('province1', None, '1', 'province', sex='男', age=30, department='省级办公室201'),
        create_user('province2', None, '1', 'province', sex='男', age=30, department='省级办公室201'),
        create_user('province3', None, '1', 'province', sex='男', age=30, department='省级办公室201')]


#encoding:utf-8
from django.contrib.auth.models import User, Group
from django.db import models


# Unused
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    blog = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=32, blank=True)
    age = models.IntegerField(max_length=2)

    ##       据说创建Admin这个内部类后，会自动有add, create   和delete三种权限
    class Admin:
        list_display = ('user', 'blog', 'email')


# Unused
class USCitizen(models.Model):
    #

    class Meta:
        permissions = (
            ("can_drive", "Can drive"),
            ("can_vote", "Can vote in elections"),
            ("can_drink", "Can drink alcohol")
        )


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    info = models.CharField(max_length=128)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(max_length=2)
    department = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s, %s" % (self.user.username, self.sex)
'''用户权限的划分

class ReservoirUser(models.Model):
    name = models.OneToOneField(User)
    group = models.ForeignKey(Group)
    def __unicode__(self):
        return self.name


class XianUser(models.Model):
    name = models.OneToOneField(User)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name


class CityUser(models.Model):
    name = models.OneToOneField(User)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name


class ProvinceUser(models.Model):
    name = models.OneToOneField(User)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name
'''
'''以下是行政区划的部分
'''
#省
class Province(models.Model):
    name = models.CharField(max_length=128)
    #cities = models.ManyToManyField(City, verbose_name="contained city")

    def __unicode__(self):
        return self.name


#市
class City(models.Model):
    name = models.CharField(max_length=128)
    province = models.ForeignKey(Province, verbose_name='belonged city')

    def __unicode__(self):
        return self.name


#县
class Xian(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, verbose_name="belonged xian")

    def __unicode__(self):
        return self.name


#水库
class Reservoir(models.Model):
    name = models.CharField(max_length=128)
    xian = models.ForeignKey(Xian, verbose_name='belonger xian')
    city = models.ForeignKey(City, verbose_name="belonger city")
    province = models.ForeignKey(Province, verbose_name="belonger province")

    def __unicode__(self):
        return "%s, %s %s %s " % (self.name, self.xian, self.city, self.province)
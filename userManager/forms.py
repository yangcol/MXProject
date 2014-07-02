from django import forms
#encoding:utf-8
__author__ = 'yangq'


class SysConfigForm(forms.Form):
    DatabaseType = forms.ChoiceField(choices=[('m', '男'), ('f', '女')])

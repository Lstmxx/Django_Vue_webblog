# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


def To_DB(obj, op, wheredict, selectdict={"*":""}):
    res = ""
    if op == "insert":
        res = obj.objects.create(**wheredict)
    elif op == "delete":
        res = obj.objects.filter(wheredict).delete()
    elif op == "update":
        res = obj.objects.filter(**wheredict).update(**selectdict)
    elif op == "query":
        if selectdict.get("*") is not None:
            res = obj.objects.values()
        else:
            res = obj.objects.filter(**wheredict).values(**selectdict)
    return res

class User(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=16,default='')
    pwd = models.CharField(max_length=32,default='')
    uid = models.AutoField(db_column='UID', primary_key=True)  # Field name made lowercase.


class Kind(models.Model):
    num = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=20)
    objects = models.Manager()


class Paper(models.Model):
    name = models.CharField(max_length=200)
    kinds = models.ForeignKey(Kind, on_delete=models.DO_NOTHING,default='')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default='')
    publish_time = models.DateTimeField('发表日期', auto_now_add=True)
    modify_time = models.DateTimeField('最后修改日期', auto_now=True)
    data = models.TextField(default="")
    # img = models.ImageField(upload_to='article_img/%Y/%m/%d/',blank=True, null=True)
    objects = models.Manager()
    source_data = models.TextField(default="")

class Image(models.Model):
    data = models.ImageField(upload_to='static/article_img/%Y/%m/%d/',blank=True, null=True)
    paper_id = models.ForeignKey(Paper,on_delete=models.DO_NOTHING,default='')
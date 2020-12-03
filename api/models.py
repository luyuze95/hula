from django.db import models

# Create your models here.


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(verbose_name='分类', max_length=32)


class Article(models.Model):
    """
    文章表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=255)
    content = models.TextField(verbose_name='文章内容')
    category_id = models.IntegerField(verbose_name='归属的分类id')

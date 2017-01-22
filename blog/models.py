from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,所以修改str类的title方法就可以实现.
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

# 文章状态
STATUS = {
        0: u'正常',
        1: u'草稿',
        2: u'删除',
}


# Create your models here.
# 导航管理
class Nav(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'导航条内容')
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'指向地址')

    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u"导航条"
        ordering = ['-create_time']
        app_label = string_with_title('blog',u"博客管理")

    def __unicode__(self):
        return self.name


# 分类管理
class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, verbose_name=u'上级分类')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'分类'
        ordering = ['rank', '-create_time']
        app_label = string_with_title('blog', u"博客管理")

    def __str__(self):
        if self.parent:
            return '%s-->%s' % (self.parent, self.name)
        else:
            return self.name


# 文章管理
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    title = models.CharField(max_length=100, verbose_name=u'标题')
    en_title = models.CharField(max_length=100, verbose_name=u'英文标题')
    img = models.CharField(max_length=200, default='/static/img/article/default.jpg')
    tags = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'标签', help_text=u'用逗号分隔')
    summary = models.TextField(verbose_name=u'摘要')
    content = RichTextField(verbose_name=u'正文')

    view_times = models.IntegerField(default=0)
    zan_times = models.IntegerField(default=0)

    is_top = models.BooleanField(default=False, verbose_name=u'置顶')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')

    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def get_tags(self):
        return self.tags.split(',')

    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['rank','-is_top','-pub_time','-create_time']
        app_label = string_with_title('blog',u"博客管理")

    def __str__(self):
        return self.title


# 专栏管理
class Column(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'专栏内容')
    summary = models.TextField(verbose_name=u'专栏摘要')
    article = models.ManyToManyField(Article, verbose_name=u'文章')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'专栏'
        ordering = ['-create_time']
        app_label = string_with_title('blog', u"博客管理")

    def __str__(self):
        return self.name


# 用户管理
class User(AbstractUser):
    img = models.CharField(max_length=200, default='/static/tx/default.jpg', verbose_name=u'头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'简介')

    class Meta(AbstractUser.Meta):
        verbose_name_plural = verbose_name = u'用户'
        app_label = string_with_title('blog', u"用户管理")


# 评论管理
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'用户')
    article = models.ForeignKey(Article,verbose_name=u'文章')
    comment = models.TextField(verbose_name=u'评论内容')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'评论'
        ordering = ['-create_time']
        app_label = string_with_title('blog', u"评论管理")

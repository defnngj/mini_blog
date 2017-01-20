# coding:utf-8
from django.contrib import admin
from blog.models import Article,Category,Carousel,Nav,Column
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from blog.models import User as BlogUser
from blog.forms import BlogUserCreationForm
from blog.models import Comment




# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('status','create_time')
    list_display = ('name','parent','rank','status')
    fields = ('name','parent','rank','status')


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title','summary')
    list_filter = ('status','category','is_top','create_time','update_time','is_top')
    list_display = ('title','category','author','status','is_top','update_time')
    fieldsets = (
        (u'基本信息', {
            'fields': ('title','en_title','img','category','tags','author','is_top','rank','status')
            }),
        (u'内容', {
            'fields': ('content',)
            }),
        (u'摘要', {
            'fields': ('summary',)
            }),
        (u'时间', {
            'fields': ('pub_time',)
            }),
    )


class NavAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','url','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','url','status')


class ColumnAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','status','article','summary')
    filter_horizontal = ('article',)


class CarouselAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','article','img','create_time')
    list_filter = ('create_time',)
    fields = ('title','article','img','summary')


class BlogUserAdmin(UserAdmin):
    add_form = BlogUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email' , 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (u'基本信息', {'fields': ('username', 'password','email')}),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('user__username','article__title','comment')
    list_filter = ('create_time',)
    list_display = ('user','article','create_time')
    fields = ('user','article','comment')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.unregister(Group)
admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Comment,CommentAdmin)


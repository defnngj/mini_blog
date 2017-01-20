from django.conf.urls import url
from blog.views import IndexView,ArticleView,AllView,SearchView,ColumnView,UserView,TagView,CategoryView
from django.views.generic import TemplateView,DetailView
from blog.views_auth import UserControl
from blog.views_comments import CommentControl


urlpatterns = [
    url(r'^$',IndexView.as_view()),
    url(r'^article/(?P<slug>\w+).html$',ArticleView.as_view()),
    url(r'^all/$',AllView.as_view()),
    url(r'^search/$',SearchView.as_view()),
    url(r'^login/$',TemplateView.as_view(template_name="blog/login.html")),
    url(r'^register/$',TemplateView.as_view(template_name="blog/register.html")),
    url(r'^forgetpassword/$',TemplateView.as_view(template_name="blog/forgetpassword.html")),
    url(r'^resetpassword/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',TemplateView.as_view(template_name="blog/resetpassword.html")),
    url(r'^column/(?P<column>\w+)$',ColumnView.as_view()),
    url(r'^user/(?P<slug>\w+)$',UserView.as_view()),
    url(r'^tag/(?P<tag>\w+)/$',TagView.as_view()),
    url(r'^category/(?P<category>\w+)/$',CategoryView.as_view()),
    url(r'^usercontrol/(?P<slug>\w+)$',UserControl.as_view()),
    url(r'^comment/(?P<slug>\w+)$',CommentControl.as_view()),
]

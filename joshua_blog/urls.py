from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_blogs.views import *
from app_accounts.views import *
from filemanager import path_end
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joshua_blog.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=r'topic_ALL_list')),
    url(r'^topic_ALL_list/$', blog_list_view),
    url(r'^(topic_ALL_list)/(\d{1,})/$', blog_list_view),
    url(r'^(blog_.*_\d{1,})/$', blog_view),
    url(r'^topic_(.*)_archive/(\d{1,})/$', blog_archive_view),
    url(r'^topic_(.*)_archive/$', blog_archive_view),
    url(r'^add_blog/$', blog_add_view),
    url(r'^update_blog_(\d{1,})/$', blog_update_view),
    url(r'^delete_blog_(\d{1,})/$', blog_delete_view),
    url(r'^add_comment_to_conversation_(\d{1,})/$', comment_add_view),
    url(r'^delete_comment_(\d{1,})/$', comment_delete_view),
    url(r'^conversation_archive/$', conversation_archive_view),
    url(r'^conversation_(\d{1,})/$', conversation_view),
    url(r'^add_conversation/$', comment_add_view),
    url(r'^accounts/login/$', account_login_view),
    url(r'^accounts/logout/$', account_logout_view),
    url(r'^filemanager/'+path_end, filemanager_view),
    url(r'^my_profile/', profile_view),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.MEDIA_URL+r'/media/favicon.ico')),
)

from django.conf.urls import patterns, include, url
from django.contrib import auth
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms_put.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'cms_2.views.personas'),
    url(r'(\d+)','cms_2.views.persona'),
    url(r'^accounts/profile', 'cms_2.views.usuario'),
    url(r'^login$','django.contrib.auth.views.login'),
    url(r'^logout$','django.contrib.auth.views.logout'),
)

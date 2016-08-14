from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medicloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('interface.urls', namespace="interface")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls', namespace="login")),
)

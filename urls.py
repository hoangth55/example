# Uncomment the next two lines to enable the admin:
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include (admin.site.urls)),
)
#urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^polls/$', 'index'),
    #(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    #(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    #(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
#)
#urlpatterns += patterns('',
#    (r'^admin/', include(admin.site.urls)),
#)


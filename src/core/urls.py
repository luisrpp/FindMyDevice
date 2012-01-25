from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^add_device/$', 'add_device', name='add_device'),
)

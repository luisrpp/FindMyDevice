from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^add_device/$', 'add_device', name='add_device'),
    url(r'^add_device/(\d+)/success$', 'success_device', name='success_device'),
    url(r'^device/(\d+)$', 'device', name='device'),
)

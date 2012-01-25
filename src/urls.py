from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Home
    (r'^$', 'core.views.homepage', {'template': 'index.html'}),
    # User profile
    url(r'^accounts/profile/$', 'core.views.profile', name='profile'),
    # Logout using django.contrib.auth
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # Django-registration
    (r'^accounts/', include('registration.urls')),
    # RESTful APIs
    (r'^api/', include('api.urls')),
    url(r'^add_device/$', 'core.views.add_device', name='add_device'),
)

urlpatterns += staticfiles_urlpatterns()

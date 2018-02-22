from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^ec/', include('ec.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ec.urls')),
]

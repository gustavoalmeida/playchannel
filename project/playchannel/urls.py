from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
)

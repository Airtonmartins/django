from django.conf.urls import patterns, include, url
from django.contrib import admin


from views import hello 
from views import post_list




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^post_list/',post_list),
 
    
)



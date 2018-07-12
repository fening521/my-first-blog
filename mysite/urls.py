from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
<<<<<<< HEAD
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
=======
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
]
>>>>>>> 71362bb07c73e10fcb2fef501841adc6b458f285

from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'about/',include('about.urls')),
    url(r'^(?P<input>[0-9]{2})/$',views.angka),
    url(r'^(?P<tahun>[0-9]{4})/$',views.tanggal),
]
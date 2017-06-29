from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^skill/$', views.skill, name='skill'),
    url(r'^p&e/$', views.pe, name='p&e'),
]

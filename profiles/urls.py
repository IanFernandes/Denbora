from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_data, name='user_data'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
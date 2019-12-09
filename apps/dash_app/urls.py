from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_registration),
    url(r'^register$',views.register),
    url(r'^login$', views.login),
    url(r'^quotes$',views.dashboard),
    url(r'^process_quote$',views.process_quote),
    url(r'^user/(?P<id>\d+)$',views.user_info),
    url(r'^user/(?P<id>\d+)/delete$', views.delete),
    url(r'^myaccount/(?P<id>\d+)$',views.edit_user),
    url(r'^process_edit_account/(?P<id>\d+)$', views.process_edit_account),
    url(r'^liked/(?P<id>\d+)$', views.liked_by),
    url(r'^logout$', views.logout),
]
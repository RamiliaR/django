from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /congratulation/
    url(r'^$', views.index, name='index'),
    # ex: /congratulation/detail/
    url(r'^detail/$', views.detail, name='detail'),
    # ex: /congratulation/order/
    url(r'^order/$', views.order, name='order'),
    # ex: /congratulation/join/
    url(r'^join/$', views.join, name='join'),
	# ex: /congratulation/add_customer/
    url(r'^add_customer/$', views.add_customer, name='add_customer'),
    # ex: /congratulation/login/
    url(r'^login/$', views.login, name='login'),
	# ex: /congratulation/logout/
    url(r'^logout/$', views.logout, name='logout'),
	# ex: /congratulation/add_order/
    url(r'^add_order/$', views.add_order, name='add_order'),
	# ex: /congratulation/information/
    url(r'^information/$', views.information, name='information'),
	# ex: /congratulation/detail/5/
    url(r'^detail/(?P<details_id>[0-9]+)/$', views.congr, name='congr'),
    # ex: /congratulation/detail/5/delete_order/
    url(r'^detail/(?P<details_id>[0-9]+)/delete_order/$', views.delete_order, name='delete_order'),
	# ex: /congratulation/detail/confirmation/
    url(r'^detail/confirmation/$', views.confirmation, name='confirmation'),
	# ex: /congratulation/detail/delete_account/
    url(r'^detail/delete_account/$', views.delete_account, name='delete_account'),
    # ex: /congratulation/detail/5/edit_order/
    url(r'^detail/(?P<details_id>[0-9]+)/edit_order/$', views.edit_order, name='edit_order'),
]
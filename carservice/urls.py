from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .view import view_car, view_cost, view_driver, view_photo, view_schedule, view_content, view_blog, view_customer
app_name = "carservice"
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^quanlyxe/$', view_car.CarList.as_view(), name='car'),
	url(r'^quanlyxe/themxe$', view_car.CarCreate.as_view(), name='car_new'),
	url(r'^quanlyxe/chitiet/(?P<pk>\d+)$', view_car.CarDetail.as_view(), name='car_detail'),
	url(r'^quanlyxe/capnhat/(?P<pk>\d+)$', view_car.CarUpdate.as_view(), name='car_edit'),
	url(r'^quanlyxe/xoa/(?P<pk>\d+)$', view_car.CarDelete.as_view(), name='car_delete'),


	url(r'^taixe/$', view_driver.driver, name='driver'),
	url(r'^taixe/themtaixe$', view_driver.driver_new, name='driver_new'),
	url(r'^taixe/chitiet/(?P<driver_id>[0-9]+)/$', view_driver.driver_detail, name='driver_detail'),
	url(r'^taixe/capnhat/(?P<driver_id>[0-9]+)/$', view_driver.driver_edit, name='driver_edit'),
	url(r'^taixe/xoa/(?P<driver_id>[0-9]+)/$', view_driver.driver_delete, name='driver_delete'),


	url(r'^album/$', view_photo.album, name='album'),
	url(r'^album/them$', view_photo.album_new, name='album_new'),
	url(r'^album/chitiet/(?P<album_id>[0-9]+)/$', view_photo.album_detail, name='album_detail'),
	url(r'^album/capnhat/(?P<album_id>[0-9]+)/$', view_photo.album_edit, name='album_edit'),
	url(r'^album/xoa/(?P<album_id>[0-9]+)/$', view_photo.album_delete, name='album_delete'),

	url(r'^anh/$', view_photo.photo, name='photo'),
	url(r'^anh/them/(?P<album_id>[0-9]+)/$$', view_photo.photo_new, name='photo_new'),
	url(r'^anh/chitiet/(?P<photo_id>[0-9]+)/$', view_photo.photo_detail, name='photo_detail'),
	url(r'^anh/capnhat/(?P<photo_id>[0-9]+)/$', view_photo.photo_edit, name='photo_edit'),
	url(r'^anh/xoa/(?P<photo_id>[0-9]+)/$', view_photo.photo_delete, name='photo_delete'),

	url(r'^lichtrinh/$', view_schedule.ScheduleList.as_view(), name='schedule'),
	url(r'^lichtrinh/them/(?P<car_id>[0-9]+)/$', view_schedule.schedule_new, name='schedule_new'),
	url(r'^lichtrinh/them/chonxe/$', view_schedule.CarList.as_view(), name='schedule_choose_car'),
	url(r'^lichtrinh/chitiet/(?P<car_id>[0-9]+)/$', view_schedule.schedule_detail, name='schedule_detail'),
	url(r'^lichtrinh/capnhat/(?P<car_id>[0-9]+)/$', view_schedule.schedule_edit, name='schedule_edit'),
	url(r'^lichtrinh/xoa/(?P<car_id>[0-9]+)/$', view_schedule.schedule_delete, name='schedule_delete'),


	url(r'^chiphi/$', view_cost.cost, name='cost'),
	url(r'^chiphi/them/$', view_cost.cost_new, name='cost_new'),
	url(r'^chiphi/chitiet/(?P<cost_id>[0-9]+)/$', view_cost.cost_detail, name='cost_detail'),
	url(r'^chiphi/capnhat/(?P<cost_id>[0-9]+)/$', view_cost.cost_edit, name='cost_edit'),
	url(r'^chiphi/xoa/(?P<cost_id>[0-9]+)/$', view_cost.cost_delete, name='cost_delete'),

	# url(r'^chiphi/json$', views.schedule_json, name='schedule_json'),
	url(r'^khachhang/$', view_customer.CustomerList.as_view(), name='customer'),
	url(r'^khachhang/them/$', view_customer.CustomerCreate.as_view(), name='customer_new'),
	url(r'^khachhang/chitiet/(?P<pk>\d+)$', view_customer.CustomerDetail.as_view(), name='customer_detail'),
	url(r'^khachhang/capnhat/(?P<pk>\d+)$', view_customer.CustomerUpdate.as_view(), name='customer_edit'),
	url(r'^khachhang/xoa/(?P<pk>\d+)$', view_customer.CustomerDelete.as_view(), name='customer_delete'),



	url(r'^dichvu/$', views.statistical_car, name='statistical_car'),
	url(r'^chiphi/$', views.statistical_income, name='statistical_income'),   
	
	# url(r'^noidung/$', view_content.content, name='content'),
	# url(r'^noidung/them$', view_content.content_new, name='content_new'),
	# url(r'^noidung/capnhat$', view_content.content_edit, name='content_edit'),   

	url(r'^noidung/$', view_content.ContentList.as_view(), name='content'),
	url(r'^noidung/them/$', view_content.ContentCreate.as_view(), name='content_new'),
	url(r'^noidung/capnhat/(?P<pk>\d+)$', view_content.ContentUpdate.as_view(), name='content_edit'),   


	url(r'^dangnhap/$', views.login, name='login'),
    url(r'^dangky/$', views.signup, name='signup'),
    # url(r'^dangnhap/$', views.login, name='login'),
    # 
    # 
    url(r'^blog/$', view_blog.BlogList.as_view(), name='blog'),
	url(r'^blog/them$', view_blog.BlogCreate.as_view(), name='blog_new'),
	url(r'^blog/chitiet/(?P<pk>\d+)$', view_blog.BlogDetail.as_view(), name='blog_detail'),
	url(r'^blog/capnhat/(?P<pk>\d+)$', view_blog.BlogUpdate.as_view(), name='blog_edit'),
	url(r'^blog/xoa/(?P<pk>\d+)$', view_blog.BlogDelete.as_view(), name='blog_delete'),
]

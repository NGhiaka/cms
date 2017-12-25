from django.conf.urls import url
 
from . import views
app_name = "frontend"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thongtin/$', views.AboutList.as_view(), name='about'),
    url(r'^datlich/$', views.BookingShow.as_view(), name='booking'),
    url(r'^datlich/tim$', views.BookingCreate.as_view(), name='create_booking'),

    url(r'^thongtinxe/$', views.CarList.as_view(), name='car'),
    url(r'^thongtinxe/(?P<pk>\d+)$', views.CarDetail.as_view(), name='detail_car'),

    url(r'^tintuc/$', views.NewsList.as_view(), name='news'),
    url(r'^tintuc/(?P<pk>\d+)$', views.NewsDetail.as_view(), name='detail_news'),
    
    url(r'^lienhe/$', views.ContactList.as_view(), name='contact'),
]
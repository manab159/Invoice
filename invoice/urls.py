from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'invoice'
urlpatterns = [
    path('', views.fetch_data, name='fetch_data'),
    url(r'^users/(?P<user_id>\d+)/$', views.fetch_invoice_data, name='fetch_invoice_data')
]

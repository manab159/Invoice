from django.urls import path

from . import views


app_name = 'invoice'
urlpatterns = [
    path('', views.fetch_data, name='fetch_data'),
]

from django.conf.urls import url
from . import views
app_name = 'dimension'
urlpatterns=[
    url(r'^$',views.dimension,name='dimension'),
    url(r'^home/$',views.dimension,name='home'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^show_base/', views.show_base_template, name='show_base_template'),
        url(r'^home/', views.home, name='home'),
        url(r'^$', views.index, name='index'),
]

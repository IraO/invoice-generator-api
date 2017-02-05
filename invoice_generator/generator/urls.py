from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.show_base_template, name='base_template'),
]

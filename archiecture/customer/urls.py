# --*-- coding: utf-8 --*--
__author__ = 'nolan'

from django.conf.urls import url
from archiecture.customer import views, tests

urlpatterns = [
    # 客户管理
    url(r'customer_list$', views.customer_list, name="customer_list"),
]

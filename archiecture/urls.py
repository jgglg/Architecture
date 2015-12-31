# --*-- coding: utf-8 --*--
"""archiecture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from archiecture.customer import urls as customer_url
from archiecture.task import urls as task_url
from archiecture.finance import urls as finance_url
from archiecture.system import urls as system_url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # 客户管理
    url(r'^customer/', include(customer_url)),
    # 任务
    url(r'^task/', include(task_url)),
    # 财务
    url(r'^finance/', include(finance_url)),
    # 系统设置
    url(r'^system/', include(system_url)),
    # 首页
    url(r'^$', include(system_url)),
]

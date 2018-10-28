from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

import bch_vpn.api as api

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/add', api.vpn.add),
]

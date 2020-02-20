# -*- coding: utf-8 -*-

"""object_detector URL Configuration."""

from django.contrib import admin
from django.urls import path

from object_detector import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.DetectObjectsAPIView.as_view()),
    path('as_method/', api.detect_objects),
]

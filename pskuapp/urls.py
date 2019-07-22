from django.urls import path, include, re_path
from django.contrib import admin

from pskuapp import views

urlpatterns = [
    path('CountryFetch/',views.CountryFetch.as_view()),
    path('ChannelFetch/',views.ChannelFetch.as_view()),
    path('CategoryFetch/',views.CategoryFetch.as_view()),
    path('BrandFetch/',views.BrandFetch.as_view()),
    path('DataFetch/',views.DataFetch.as_view()),
    path('UpdatePSKU/',views.UpdatePSKU.as_view()),
    path('UpdateTargetWD/',views.UpdateTargetWD.as_view()),
]

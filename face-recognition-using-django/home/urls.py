from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^addFace/', views.addFace),
    url(r'^welcome/(?P<face_id>\d+)/$', views.welcome),
    url(r'^configuration/', views.configuration),
    url(r'^configerror/',views.configMissing)
]

from django.conf.urls import url, include
from app02 import views
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^publish_list/$', views.publish_list,name="publishnew"),
    url(r'^book_list/', views.book_list,name="booknew"),
    url(r'^publish_add/', views.Addpub.as_view(),name="addpublish"),
    url(r'^del_(booknew|publishernew)/(\d+)/$', views.delete,name="del"),
]

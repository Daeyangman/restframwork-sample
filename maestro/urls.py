from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views
# router = DefaultRouter()
# router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # url(r'', include(router.urls)),
    url(r'^post/$' , views.PostList.as_view())
]


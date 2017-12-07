from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^post/$' , views.PostListAPIView.as_view()),
    url(r'^eeg/$', views.EEGListView.as_view() , name = "eeg"),
    url(r'^login_end/$', views.LoginendTemplateView.as_view(), name="login_end"),
    url(r'^mypage/$', views.MypageTemplateView.as_view(), name="mypage")

]
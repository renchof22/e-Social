from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('setting/', views.PlayerCreateView.as_view(template_name='app1/setting.html'), name='setting'),
    path('clan/create/', views.ClanCreateView.as_view(template_name='app1/clan_create.html'), name='clan_create'),
    path('mypage/', views.MyPage.as_view(template_name='app1/mypage.html'), name='mypage'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]

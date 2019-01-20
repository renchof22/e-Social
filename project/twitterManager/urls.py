from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    # リダイレクトページ
    path('top/', views.top_page, name="top"),
    # ログインページ
    path('login/', LoginView.as_view(template_name='twitterManager/login.html'), name='login'),
    # ログアウトページ
    path('logout/', LogoutView.as_view(template_name='twitterManager/logout.html'), name='logout'),
]

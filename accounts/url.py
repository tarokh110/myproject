from django.urls import path, include, re_path
from django.contrib import admin
from . import views
from django.contrib import auth
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [

    path('signUp/', views.signUp, name='signUp'),
    path('dashboard/', views.profile, name='profile'),
    # path('login/', views.log_in, name='log_in' ),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('blog/post/list', views.post_list, name='post_list'),
    path('blog/<int:id>/', views.post_detail, name='post_detail')
    #  reuqest mikhad be onvane argu ke to pdf nabood hamchin chizi !   path('logout-then-login', auth_views.logout_then_login(request='', login_url='registration/login.html'), name='logout-then-login'),

]

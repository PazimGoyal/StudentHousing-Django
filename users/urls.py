from django.urls import path

from . import views
from django.contrib.auth import views as view


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login_ad_post/', views.login_post_ad, name='login_post_ad'),
    path('like/',views.likes,name='like'),
    path('editProfile/', views.edit_profile, name='editProfile'),

    path('password-change/', view.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', view.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password-reset/', view.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

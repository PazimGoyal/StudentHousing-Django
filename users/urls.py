from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login_ad_post/', views.login_post_ad, name='login_post_ad'),
    path('like/',views.likes,name='like'),

]

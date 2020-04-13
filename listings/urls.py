from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addListing/', views.add_item, name='addListing'),
    path('<int:request_id>', views.single_listing, name='id2'),
    path('listings/<int:request_id>', views.single_listing, name='id'),
    path('listings/', views.listings, name='listings'),
    path('email/', views.mail_sending, name='email'),
    path('edit/<int:request_id>', views.edit_listing, name='edit'),
    path('delete/<int:request_id>', views.delete_listing, name='delete'),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('addListing/', views.add_item, name='addListing'),
    path('<int:request_id>', views.listing, name='id2'),
    path('search/<int:request_id>', views.listing, name='id'),
    path('search/', views.search_lisitng, name='search'),

]

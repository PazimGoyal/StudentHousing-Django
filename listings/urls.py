from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addListing/',views.add_item),
    path('<int:request_id>', views.listing)

]
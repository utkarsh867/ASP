from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('orders/', views.ordered_list, name='orders'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('notify_delivery/', views.notify_delivery, name='orders'),
    path('cancel_order/', views.cancel_order, name='cancel_order')
]
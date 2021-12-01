from django.urls import path
from .import views
print("urls called")

urlpatterns = [
    path('', views.index,name='index'),
    path('watches/',views.watches,name='watches'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_watches/',views.add_watches,name='add_watches'),
    path('view_watches/',views.view_watches,name='view_watches'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('watch_detail/<int:pk>/',views.watch_detail,name='watch_detail'),
    path('watch_edit/<int:pk>/',views.watch_edit,name='watch_edit'),
    path('watch_delete/<int:pk>/',views.watch_delete,name='watch_delete'),
    path('user_watch_detail/<int:pk>/',views.user_watch_detail,name='user_watch_detail'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('mywishlist/',views.mywishlist,name='mywishlist'),
    path('remove_wishlist/<int:pk>/',views.remove_wishlist,name='remove_wishlist'),
    path('mycart/',views.mycart,name='mycart'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'), 
    path('remove_cart/<int:pk>/',views.remove_cart,name='remove_cart'),
    path('change_qty/',views.change_qty,name='change_qty'),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'), 
    path('validate_email/',views.validate_email,name='validate_email'),  
]
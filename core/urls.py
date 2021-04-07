from django.urls import path,include
from core.views import *
urlpatterns = [
   path('',dashboard,name='home'),
   path('customer_detail/<str:slug>',customer_single,name='customer_detail'),
   path('product/',product),
   path("add_order/",CreateOrder, name="add_order"),
   path("add_order_specific/<str:slug>",CreateOrder_specific, name="add_order_specific"),
   path("update_order/<str:slug>",updateOrder, name="update_order"),
   path("delete_order/<int:id>",deleteOrder, name="delete_order"),
   path("register",RegisterUser,name='register'),
   path("login",LoginUser,name='login'),
   path("logout",LogoutUser,name='logout'),
   path('user_page',UserPage,name='user_page'),

]

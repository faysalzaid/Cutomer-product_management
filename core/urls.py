from django.urls import path,include
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('',dashboard,name='home'),
   path('customer_detail/<str:slug>',customer_single,name='customer_detail'),
   path('product',product),
   path("add_order",CreateOrder, name="add_order"),
   path("add_order_specific/<str:slug>",CreateOrder_specific, name="add_order_specific"),
   path("update_order/<str:slug>",updateOrder, name="update_order"),
   path("delete_order/<int:id>",deleteOrder, name="delete_order"),
   path("register",RegisterUser,name='register'),
   path("login",LoginUser,name='login'),
   path("logout",LogoutUser,name='logout'),
   path('user_page',UserPage,name='user_page'),
   path("order/<str:slug>",Order_single_view, name="order"),
   path('settings',UserSettings,name='settings'),
   path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
   path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
   path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
   path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
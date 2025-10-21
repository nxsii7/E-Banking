from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='home'),
    path('register/',views.register,name='register'),
    path('account/',views.account,name='account'),
    path('transaction/',views.transaction,name='transaction'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('login/',views.login,name='login'),
    path('base/',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('home_base/',views.home_base,name='home_base'),
    path('addm_oney/',views.add_money,name='add_money'),
    path('transfer/',views.tranfer,name='transfer'),
    path('pay/',views.pay,name='pay'),
    path('payment/',views.payment,name='payment'),
    path('pin_base/',views.pin_base,name='pin_base'),
 
    


    
    
]


# from django.conf.urls import url
from django.urls import path
from UserApp import views

urlpatterns = [
    # url(r'^user$', views.userAPI),
    # url(r'^user/([0-9]+)$', views.userAPI),
    # url(r'^payment$', views.paymentAPI),
    # url(r'^payment/([0-9]+)$', views.paymentAPI),
    path('user', views.userAPI),
    path('user/<int:id>', views.userAPI),
    path('payment', views.paymentAPI),
    path('payment/<int:id>', views.paymentAPI),
]
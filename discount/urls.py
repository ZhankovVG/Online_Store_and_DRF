from django.urls import path
from . import views


app_name = 'discount'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),
]
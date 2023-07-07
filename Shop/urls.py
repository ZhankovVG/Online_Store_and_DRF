from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', views.CategoryView.as_view(), name='category')
]
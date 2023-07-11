from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('category/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),
    path('search', views.SearchView.as_view(), name='search'),
    path('comments<int:pk>/', views.CommentsView.as_view(), name='comments'),
]

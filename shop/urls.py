from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('category/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),
    path('search', views.SearchView.as_view(), name='search'),
    path('comments<int:pk>/', views.CommentsView.as_view(), name='comments'),
    # Added URLs for DRF API
    path('api/v1/product/', views.ProductApiListView.as_view()),
    path('api/v1/product/<int:pk>/', views.ProductApiDetailView.as_view()),
    path('api/v1/review/', views.ReviewApiView.as_view()),
]

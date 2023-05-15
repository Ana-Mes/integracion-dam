from django.urls import path
from . import views

reviews_patterns = ([
    path('', views.ReviewListView.as_view(), name="reviews"),
    path('<int:pk>/<slug:slug>/', views.ReviewDetailView.as_view(), name="review"),
    path('create/', views.DivingSpotCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.DivingSpotUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.DivingSpotDelete.as_view(), name='delete'),
], 'reviews')
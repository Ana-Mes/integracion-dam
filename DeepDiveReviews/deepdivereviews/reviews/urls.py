from django.urls import path
from .views import ReviewListView, ReviewDetailView, DivingSpotCreate

reviews_patterns = ([
    path('', ReviewListView.as_view(), name="reviews"),
    path('<int:pk>/<slug:slug>/', ReviewDetailView.as_view(), name="review"),
    path('create/', DivingSpotCreate.as_view(), name="create"),
], 'reviews')
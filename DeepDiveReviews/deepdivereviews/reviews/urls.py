from django.urls import path
from .views import ReviewListView, ReviewDetailView, DivingSpotCreate, DivingSpotUpdate, DivingSpotDelete

reviews_patterns = ([
    path('', ReviewListView.as_view(), name="reviews"),
    path('<int:pk>/<slug:slug>/', ReviewDetailView.as_view(), name="review"),
    path('create/', DivingSpotCreate.as_view(), name="create"),
    path('update/<int:pk>/', DivingSpotUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', DivingSpotDelete.as_view(), name='delete'),
], 'reviews')
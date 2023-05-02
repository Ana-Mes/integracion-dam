from django.urls import path
from .views import ReviewListView

reviews_patterns = [
    path('', ReviewListView.as_view(), name="reviews"),
]
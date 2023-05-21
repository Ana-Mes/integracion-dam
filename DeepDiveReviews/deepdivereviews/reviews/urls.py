from django.urls import path, include
from . import views

app_name = 'reviews'

divingspot_patterns = [
    path('', views.ReviewListView.as_view(), name="review_home"),
    path('search-reviews', views.ReviewSearchView.as_view(), name="review_search"),
    path('<int:pk>/<slug:slug>/', views.ReviewDetailView.as_view(), name="review_detail"),
    path('create/', views.DivingSpotCreate.as_view(), name="review_create"),
    path('update/<int:pk>/', views.DivingSpotUpdate.as_view(), name='review_update'),
    path('delete/<int:pk>/', views.DivingSpotDelete.as_view(), name='review_delete'),
]
comments_patterns = [
    path('update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
]

urlpatterns = [
    path('', include(divingspot_patterns)),
    path('comment', include(comments_patterns)),
]

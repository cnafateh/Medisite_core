from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns = [
    # path("categories/", CategoryListCreateAPIView.as_view(), name="category-list"),
    # path("categories/<int:pk>/", CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-detail"),
    path("posts/", PostListCreateAPIView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view(), name="post-detail"),
]

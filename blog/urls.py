from django.urls import path
from  .views import renderPosts, post_detail

urlpatterns = [
    path("", renderPosts, name="posts"),
    path("<int:post_id>", post_detail),
]
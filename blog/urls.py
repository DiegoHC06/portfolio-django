from django.urls import path
from  .views import renderPosts

urlpatterns = [
    path("", renderPosts, name="posts"),
    # path("<int:post_id>", views.post_detail, name="post_detail"),
]
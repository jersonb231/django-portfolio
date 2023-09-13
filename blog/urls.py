from django.urls import path
from .views import render_posts, pos_detail

app_name="blog"

urlpatterns = [
    path ('', render_posts, name='posts'),
    path("<int:post_id>", pos_detail, name="post_detail"),
]